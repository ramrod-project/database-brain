from .brain.checks import verify, strip
from .brain import brain_pb2 as b

GoodCommand = {"CommandName": "anystring", 
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

BadCommand = {"CommandName": 135465134, 
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

BadCommand2 = {"CommandName": "string", 
              "Tooltip": 465,
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand3 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": "heyimnotsupposedtobeastring",
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand4 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : 2167854389265, 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand5 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": 135461534653,
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand6 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": 248908938209,
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand7 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": 647238}],
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand8 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : 4564,
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand9 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": 123465,
                                  "Tooltip": "String",
                                  "Value": "String"}]}

BadCommand10 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": 123456,
                                  "Value": "String"}]}

BadCommand11 = {"CommandName": "string", 
              "Tooltip": "stringy thing",
              "Output": True,
              "Inputs": [{"Name" : "string", 
                          "Type": "String",
                          "Tooltip": "String",
                          "Value": "String"}], 
              "OptionalInputs": [{"Name" : "string",
                                  "Type": "String",
                                  "Tooltip": "String",
                                  "Value": 132456}]}

def test_good_command():
    assert verify(GoodCommand, b.Command())

def test_bad_command():
    assert not verify(BadCommand, b.Command())

def test_bad_command2():
    assert not verify(BadCommand2, b.Command())

def test_bad_command3():
    assert not verify(BadCommand3, b.Command())

def test_bad_command4():
    assert not verify(BadCommand4, b.Command())

def test_bad_command5():
    assert not verify(BadCommand5, b.Command())

def test_bad_command6():
    assert not verify(BadCommand6, b.Command())

def test_bad_command7():
    assert not verify(BadCommand7, b.Command())

def test_bad_command8():
    assert not verify(BadCommand8, b.Command())

def test_bad_command9():
    assert not verify(BadCommand9, b.Command())

def test_bad_command10():
    assert not verify(BadCommand10, b.Command())

def test_bad_command11():
    assert not verify(BadCommand11, b.Command())
