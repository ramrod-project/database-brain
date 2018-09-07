"""
Query module is getting big
"""

# import here for backward compatible
from ..static import RBT, RBJ, RBO, RBF, RPX, RPC, RPP


COMMAND_NAME_KEY = "CommandName"

# backward compatible api
from .reads import *
from .writes import *
