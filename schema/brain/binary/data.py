"""
functions related to moving binary objects in/out of Brain.Files
"""

from .. import r
from ..queries.decorators import wrap_connection, wrap_rethink_errors
from ..checks import verify
from ..brain_pb2 import Binary
from ..queries import RBF
from .decorators import wrap_name_to_id, PRIMARY_FIELD

BINARY = r.binary


@wrap_rethink_errors
@wrap_name_to_id
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
    """

    :param filename:
    :param conn:
    :return: <dict>
    """
    return RBF.get(filename).run(conn)


@wrap_rethink_errors
@wrap_connection
def list_dir(conn=None):
    """

    :param conn:
    :return: <list>
    """
    available = RBF.pluck(PRIMARY_FIELD).run(conn)
    return [x[PRIMARY_FIELD] for x in available]


@wrap_rethink_errors
@wrap_connection
def delete(filename, conn=None):
    """
    deletes a file
    filename being a value in the "id" key
    :param filename: <str>
    :param conn: <rethinkdb.DefaultConnection>
    :return: <dict>
    """
    return RBF.get(filename).delete().run(conn)
