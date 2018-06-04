from .brain.checks import verify, strip
from .brain import brain_pb2 as b

Good_TARGET = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "Optional" : "anything",
}

def test_good_target():
    assert verify(Good_TARGET, b.Target())
    