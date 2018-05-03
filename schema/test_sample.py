from brain import brain_pb2 as b
from google.protobuf.message import EncodeError
import dict_to_protobuf

dict_to_protobuf.l.setLevel("ERROR")

SAMPLE_TARGET = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "CompletelyUnrelatedKey": False,
}
FILTERED_OUTPUT = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
}


def verify(value, msg):
    """
    C-style validator

    Keyword arguments:
    value -- dictionary to validate (required)
    msg -- the protobuf schema to validate against (required)

    Returns:
        True: If valid input
        False: If invalid input
    """
    result = True
    dict_to_protobuf.dict_to_protobuf(value, msg)
    try:
        msg.SerializeToString()
    except EncodeError:
        result = False
    return result

def filter(value, msg):
    raise NotImplementedError("filtering implemented later")

def test_verify():
    assert (verify(SAMPLE_TARGET, b.Target()))
def test_filter():
    from pytest import raises
    with raises(NotImplementedError):
        output = filter(SAMPLE_TARGET, b.Target())


if __name__ == "__main__":
    from sys import stderr, argv
    stderr.write("run tests with 'pytest %s'" %(argv[0]))
    test_verify()
    test_filter()