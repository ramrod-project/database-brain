"""

"""

from .. import r
from ..queries.decorators import wrap_connection, wrap_rethink_errors
from ..checks import verify
from ..brain_pb2 import Binary
from ..queries import RBF

BINARY = r.binary
PRIMARY_FIELD = "Name"


@wrap_rethink_errors
@wrap_connection
def put(obj_dict, conn=None, **kwargs):
    """

    :param obj_dict: <dict> matching brain_pb2.Binary object
    :param conn:
    :param kwargs:
    :return:
    """
    if kwargs.get("verify", False):
        verify(obj_dict, Binary())
    inserted = RBF.insert(obj_dict).run(conn)
    return inserted


@wrap_rethink_errors
@wrap_connection
def get(filename, conn=None):
    return RBF.get(filename).run(conn)


@wrap_rethink_errors
@wrap_connection
def list_dir(conn=None):
    available = RBF.pluck(PRIMARY_FIELD).run(conn)
    return [x[PRIMARY_FIELD] for x in available]


@wrap_rethink_errors
@wrap_connection
def delete(filename, conn=None):
    return RBF.get(filename).delete().run(conn)
