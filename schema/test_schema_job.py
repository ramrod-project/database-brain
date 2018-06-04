from .brain.checks import verify, strip
from .brain import brain_pb2 as b
from .test_schema_target import Good_TARGET
from .test_schema_command import GoodCommand

Goodjob = {"id": "string",
           "JobTarget": Good_TARGET,
           "Status": "string",
           "StartTime": 0,
           "JobCommand": GoodCommand,}

def test_good_job():
    assert verify(Goodjob, b.Job())