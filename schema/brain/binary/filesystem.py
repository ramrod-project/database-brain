"""
requires fuse
"""

from sys import stderr
import stat
from multiprocessing import Lock
from time import time
from collections import defaultdict
from io import BytesIO
from time import sleep

noop = lambda *args, **kwargs: None  # :pragma-nocover #PEP-559


try:
    from fuse import FUSE, FuseOSError, Operations, c_stat, ENOENT, LoggingMixIn
    has_fuse = True
except ImportError as import_error:
    err_str = str(import_error)
    stderr.write("{1} - {0} requires fuse\n".format(__name__, err_str))
    has_fuse = False
    FUSE = noop
    FuseOSError = None
    Operations = object
    c_stat = object

from .data import get, put, BINARY

VERBOSE = False
GET_DIR = [".", "..", "GOOD_TEST"]
READ_ONLY = False
MAX_CACHE_TIME = 600


class NoStat(c_stat):
    def __init__(self):
        self.staged = False
        self.st_mode = 0
        self.st_ino = 0
        self.st_dev = 0
        self.st_nlink = 2
        self.st_uid = 0
        self.st_gid = 0
        self.st_size = 0
        self.st_atime = 0
        self.st_mtime = 0
        self.st_ctime = 0

    def as_dict(self):
        return dict((key, getattr(self, key)) for key in ('st_atime',
                                                          'st_ctime',
                                                          'st_mtime',
                                                          'st_gid',
                                                          'st_mode',
                                                          'st_nlink',
                                                          'st_size',
                                                          'st_uid',
                                                          'st_ino'))


class BrainStore(LoggingMixIn, Operations):
    """
    read only filesystem
    getattr should raise FuseOSError(ENOENT) when brain file doesn't exist
       and
    implement the create/write functions to be r/w
    """
    def __init__(self):
        self.cache = dict()
        self.attr = defaultdict(dict)
        self.attr_lock = Lock()

    def read(self, path, size, offset, fh):
        # print("read {}".format(path))
        return self.cache[path][offset:offset+size]

    def getattr(self, path, fh=None):
        # print("attr {}".format(path))
        with self.attr_lock:
            filename = path.strip("/")
            now_time = time()
            if now_time - self.attr[path].get("ts", 0) > MAX_CACHE_TIME:
                base = NoStat()
                brain_data = get(filename) or {}
                if not brain_data and not READ_ONLY:
                    raise FuseOSError(ENOENT)
                buf = brain_data.get("Content", b"")
                base.st_mode = stat.S_IFREG | 0o755
                base.st_nlink = 1
                base.st_size = len(buf)
                self.cache[path] = buf
                self.attr[path] = {"ts": now_time, "base": base, "staged": None}
            else:
                base = self.attr[path]['base']
        return base.as_dict()

    def create(self, path, mode):
        """
        This is currently a read-only filessytem.
        GetAttr will return a stat for everything
        if getattr raises FuseOSError(ENOENT)
        OS may call this function and the write function
        """
        # print("create {}".format(path))
        now_time = time()
        with self.attr_lock:
            base = NoStat()
            base.staged = True
            base.st_mode = stat.S_IFREG | 0o755
            base.st_nlink = 1
            base.st_size = -1
            self.attr[path] = {"ts": now_time, "base": base, "staged": BytesIO()}
        return mode

    def write(self, path, data, offset, fh):
        """
        This is a readonly filesystem right now
        """
        # print("write {}".format(path))
        with self.attr_lock:
            base = self.attr[path]['base']
            staged = self.attr[path]['staged']
            if not staged.closed:
                base.st_size += len(data)
                staged.write(data)
        return len(data)

    def release(self, path, fh):
        # print("release {}".format(path))
        with self.attr_lock:
            base = self.attr[path]['base']
            filename = path.strip("/")
            staged = self.attr[path]["staged"]
            if base.staged and base.st_size > 0 and not staged.closed:
                io_val = staged.getvalue()
                staged.close()
                put({"id": filename, "Name": filename, "Content": BINARY(io_val)})
                del self.attr[path]
        self._cleanup()
        return 0

    def _cleanup(self):
        """
        cleans up data that's been in the cache for a while

        should be called from an async OS call like release? to not impact user
        :return:
        """
        need_to_delete = []  # can't delete from a dict while iterating
        with self.attr_lock:
            now_time = time()
            for path in self.cache:
                if now_time - self.attr[path]['ts'] >= MAX_CACHE_TIME:
                    need_to_delete.append(path)
            for path in need_to_delete:
                del self.attr[path]
                del self.cache[path]


def start_filesystem(mountpoint):
    if has_fuse:
        FUSE(BrainStore(), mountpoint,  foreground=True)
    else:
        raise ImportError(err_str)


