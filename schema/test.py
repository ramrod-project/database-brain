from brain import brain_pb2 as b

def verify(value, msg):
    """
    C-style validator

    Keyword arguments:
    value -- the real part (required)
    imag -- the imaginary part (required)

    Returns:
        True: If valid input
        False: If invalid input
    """
    from google.protobuf.message import EncodeError
    from dict_to_protobuf import dict_to_protobuf as d2p
    result = True
    d2p(value, msg)
    try:
        msg.SerializeToString()
    except EncodeError:
        result = False
    return result

if __name__ == "__main__":
    sample_target = {
        "PluginName": "WaterBalloon",
        "Location": "Patio",
        "Port": "West"
    }
    assert (verify(sample_target, b.Target()))