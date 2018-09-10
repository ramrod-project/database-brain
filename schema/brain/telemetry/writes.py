"""
functions required to put/update telemetry
"""

from ..queries.decorators import wrap_connection, wrap_rethink_errors
from ..brain_pb2 import Telemetry
from ..checks import verify
from ..static import TARGET_OPTIONAL_FIELD
from ..static import RBT
from . import COMMON_FIELD, SPECIFIC_FIELD


def update_telemetry(target_id,
                     specific=None, common=None,
                     verify_telemetry=False, conn=None):
    specific_out = update_specific(target_id, specific, conn)
    common_out = update_common(target_id, common, verify_telemetry, conn)
    return specific_out, common_out


@wrap_rethink_errors
@wrap_connection
def update_specific(target_id, specific, conn=None):
    output = {}
    if specific:
        data = {TARGET_OPTIONAL_FIELD: {SPECIFIC_FIELD: specific}}
        output = RBT.get(target_id).update(data).run(conn)
    return output


@wrap_rethink_errors
@wrap_connection
def update_common(target_id, common,
                  verify_telemetry=False, conn=None):
    output = {}
    if common and verify_telemetry and verify(common, Telemetry.common()):
        data = {TARGET_OPTIONAL_FIELD: {COMMON_FIELD: common}}
        output = RBT.get(target_id).update(data).run(conn)
    return output
