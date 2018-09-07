"""
module holds static variables thay may be used elsewhere

"""
from . import r

COMMAND_FIELD = "JobCommand"
INPUT_FIELD = "Inputs"
OPTIONAL_FIELD = "OptionalInputs"
VALUE_FIELD = "Value"
STATUS_FIELD = "Status"
START_FIELD = "StartTime"
TARGET_OPTIONAL_FIELD = "Optional"

BEGIN = ""
INVALID = "Invalid"
VALID = "Valid"
READY = "Ready"
STOP = "Stopped"
PENDING = "Pending"
DONE = "Done"
ERROR = "Error"
WAITING = "Waiting"
ACTIVE = "Active"

SUCCESS = "success"
FAILURE = "failure"
TRANSITION = "transition"


BRAIN_DB = "Brain"
AUDIT_DB = "Audit"
PLUGINDB = "Plugins"
CONTROLLER_DB = "Controller"
JOBS = "Jobs"
TARGETS = "Targets"
OUTPUTS = "Outputs"
FILES = "Files"
TARGET = "Target"
PLUGIN = "Plugin"
PLUGINS_TABLE = "Plugins"
PORTS_TABLE = "Ports"


LOGLEVEL_KEY = "LOGLEVEL"
STAGE_KEY = "STAGE"

PROD = "PROD"
QA = "QA"
DEV = "DEV"
TESTING = "TESTING"
STAGES = {PROD: 0,
          QA: 1,
          DEV: 2,
          TESTING: 3}


RBT = r.db(BRAIN_DB).table(TARGETS)
RBJ = r.db(BRAIN_DB).table(JOBS)
RBO = r.db(BRAIN_DB).table(OUTPUTS)
RBF = r.db(BRAIN_DB).table(FILES)
RPX = r.db(PLUGINDB)
RPC = r.db(CONTROLLER_DB).table(PLUGINS_TABLE)
RPP = r.db(CONTROLLER_DB).table(PORTS_TABLE)
