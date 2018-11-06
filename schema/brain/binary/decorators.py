"""
decorators fro the binary module
"""
from decorator import decorator
from .. import r
from collections import Counter
# import magic at bottom of file

BINARY = r.binary
from . import PRIMARY_FIELD, PRIMARY_KEY, \
    CONTENT_FIELD, CONTENTTYPE_FIELD

MEGA_BYTE = 1048576
MAX_PUT = MEGA_BYTE * 95

@decorator
def wrap_name_to_id(func_, *args, **kwargs):
    """
    destination (rethinkdb) needs the id field as primary key
    put the Name field into the ID field
    :param func_:
    :param args:
    :param kwargs:
    :return:
    """
    assert isinstance(args[0], dict)
    args[0][PRIMARY_KEY] = args[0].get(PRIMARY_FIELD, "")
    return func_(*args, **kwargs)

@decorator
def wrap_split_big_content(func_, *args, **kwargs):
    obj_dict = args[0]
    if len(obj_dict["Content"]) < MAX_PUT:
        obj_dict["Part"] = False
        return func_(*args, **kwargs)
    else:
        start_point = 0
        file_count = 0
        new_dict = {}
        resp_dict = Counter({})
        file_list = []
        while start_point < len(obj_dict["Content"]):
            file_count += 1
            new_dict["Name"] = obj_dict["Name"] + str(file_count)
            file_list.append(new_dict["Name"])
            new_dict["ContentType"] = obj_dict["ContentType"]
            new_dict["Timestamp"] = obj_dict["Timestamp"]
            end_point = file_count * MAX_PUT
            new_dict["Content"] = obj_dict["Content"][start_point : end_point]
            new_dict["Part"] = True
            start_point = end_point
            new_args = (new_dict, args[1])
            resp_dict += Counter(func_(*new_args, **kwargs))

        obj_dict["Content"] = b""
        obj_dict["Parts"] = file_list
        new_args = (obj_dict, args[1])
        resp_dict += Counter(func_(*new_args, **kwargs))
        return resp_dict

@decorator
def wrap_guess_content_type(func_, *args, **kwargs):
    """
    guesses the content type with libmagic if available
    :param func_:
    :param args:
    :param kwargs:
    :return:
    """
    assert isinstance(args[0], dict)
    if not args[0].get(CONTENTTYPE_FIELD, None):
        content = args[0].get(CONTENT_FIELD, b"")
        try:
            args[0][CONTENTTYPE_FIELD] = magic.from_buffer(content)
        except magic.MagicException:  # pragma: no cover
            args[0][CONTENTTYPE_FIELD] = MockMagic.DEFAULT_MAGIC
    return func_(*args, **kwargs)


@decorator
def wrap_content_as_binary_if_needed(func_, *args, **kwargs):
    """
    destination (rethinkdb) needs the id field as primary key
    put the Name field into the ID field
    :param func_:
    :param args:
    :param kwargs:
    :return:
    """
    assert isinstance(args[0], dict)
    try:
        args[0][CONTENT_FIELD] = BINARY(args[0].get(CONTENT_FIELD, b""))
    except (r.errors.ReqlDriverCompileError, AttributeError):  # pragma: no cover
        pass  # toss in the object as string
    return func_(*args, **kwargs)


class MockMagic(object):  # pragma: no cover
    """
    class to simulate libmagic  if not available
    """
    DEFAULT_MAGIC = "data"

    class MagicException(Exception):  # pragma: no cover
        """
        exception mapped to libmagic.MagicExeption
        """
        pass

    @staticmethod
    def from_buffer(content=None):  # pragma: no cover
        """
        matches python-magic from_buffer api
        :param content: <iterable>
        :return: always returns DEFAULT_MAGIC
        """
        return MockMagic.DEFAULT_MAGIC


try:
    import magic
except ImportError:  # pragma: no cover
    magic = MockMagic
