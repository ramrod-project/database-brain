from .brain.checks import verify, strip
from .brain import brain_pb2 as b

Dictionary = {"CommandName": "anystring", 
              "Tooltip": "otherstring",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}
def test_good_command():
    assert verify(Dictionary, b.Command())

