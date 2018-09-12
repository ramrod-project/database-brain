from .brain.checks import verify, strip
from .brain import brain_pb2 as b

Good_TARGET = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "Optional": {"anything": "anything"},
}
Good_TARGET2 = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "Optional": {"Common": {"Admin": True,
                            "User": "hi"}},
}
Good_TARGET3 = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "Optional": {"Common": {"Admin": True,
                            "User": "hi"},
                 "Specific": {"CouldBeAnything": [0, "or nothing"]}},
}

Bad_TARGET = {
    "PluginName": 456,
    "Location": "Patio",
    "Port": "West",
    "Optional": "anything",
}

Bad_TARGET2 = {
    "PluginName": "WaterBalloon",
    "Location": 456,
    "Port": "West",
    "Optional": "anything",
}

Bad_TARGET3 = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": 456,
    "Optional": "anything",
}

Bad_TARGET4 = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "Optional": True,
}

Bad_TARGET5 = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "Optional": {"Common":
                     {"Checkin": None}  # should be a number
                 },
}
Bad_TARGET6 = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "Optional": {
        "init": None  # should be a string
    },
}

def test_good_target():
    assert verify(Good_TARGET, b.Target())


def test_good_target2():
    assert verify(Good_TARGET2, b.Target())


def test_good_target3():
    assert verify(Good_TARGET3, b.Target())


def test_bad_target():
    assert not verify(Bad_TARGET, b.Target())


def test_bad_target2():
    assert not verify(Bad_TARGET2, b.Target())


def test_bad_target3():
    assert not verify(Bad_TARGET3, b.Target())


def test_bad_target4():
    assert not verify(Bad_TARGET4, b.Target())


def test_bad_target5():
    assert not verify(Bad_TARGET5, b.Target())


def test_bad_target6():
    assert not verify(Bad_TARGET6, b.Target())
