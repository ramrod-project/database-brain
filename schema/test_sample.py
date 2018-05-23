from brain import brain_pb2 as b
from google.protobuf.message import EncodeError
import dict_to_protobuf #this lib allows extra keys
dict_to_protobuf.l.setLevel("ERROR")

SAMPLE_TARGET = {
    "PluginName": "WaterBalloon",
    "Location": "Patio",
    "Port": "West",
    "CompletelyUnrelatedKey": False,
}
SAMPLE_BAD_TARGET = {
    "PluginName": "WaterBalloon",
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

def strip(value, msg):
    dict_to_protobuf.dict_to_protobuf(value, msg)
    msg.SerializeToString()  #raise error for insufficient input
    output = dict_to_protobuf.protobuf_to_dict(msg)
    return output

def test_verify():
    assert (verify(SAMPLE_TARGET, b.Target()))

def test_no_verify():
    assert (not verify(SAMPLE_BAD_TARGET, b.Target()))


def test_strip():
    output = strip(SAMPLE_TARGET, b.Target())
    for key, value in output.items():
        assert ( output[key] == FILTERED_OUTPUT[key] )


if __name__ == "__main__":
    from sys import stderr, argv
    stderr.write("run tests with 'pytest %s'" %(argv[0]))
    test_verify()
    test_no_verify()
    test_strip()