"""

"""
from .brain.checks import verify
from .brain import brain_pb2 as b
from uuid import uuid4
from copy import deepcopy


plugin1_controller = {
    "id": "1-1-A",
    "Name": "Plugin1",
    "ServiceName": str(uuid4()),
    "State": "Available",
    "DesiredState": "",
    "OS": "posix",
    "Interface": "192.16.5.240",
    "ExternalPorts": ["9999/tcp"],
    "InternalPorts": ["9999/tcp"],
    "Environment": ["STAGE=DEV"]
}


plugin1_controller_empty_ports = {
    "id": "1-1-A",
    "Name": "Plugin1",
    "ServiceName": str(uuid4()),
    "State": "Available",
    "DesiredState": "",
    "OS": "posix",
    "Interface": "192.16.5.240",
    "ExternalPorts": [],
    "InternalPorts": [],
    "Environment": ["STAGE=DEV"]
}


def test_good_plugin():
    assert verify(plugin1_controller, b.Plugin())


def test_empty_ports():
    assert verify(plugin1_controller_empty_ports, b.Plugin())


def test_no_id():
    p = deepcopy(plugin1_controller)
    del p['id']
    assert verify(p, b.Plugin())


def test_no_name():
    p = deepcopy(plugin1_controller)
    del p['Name']
    assert not verify(p, b.Plugin())


def test_no_servicename():
    p = deepcopy(plugin1_controller)
    del p['ServiceName']
    assert not verify(p, b.Plugin())


def test_no_state():
    p = deepcopy(plugin1_controller)
    del p['State']
    assert not verify(p, b.Plugin())


def test_no_dstate():
    p = deepcopy(plugin1_controller)
    del p['DesiredState']
    assert not verify(p, b.Plugin())


def test_no_os():
    p = deepcopy(plugin1_controller)
    del p['OS']
    assert not verify(p, b.Plugin())


def test_no_if():
    p = deepcopy(plugin1_controller)
    del p['Interface']
    assert not verify(p, b.Plugin())


def test_no_ports():
    p = deepcopy(plugin1_controller)
    del p['ExternalPorts']
    assert not verify(p, b.Plugin())


def test_no_iports():
    p = deepcopy(plugin1_controller)
    del p['InternalPorts']
    assert not verify(p, b.Plugin())


def test_bad_ports():
    p = deepcopy(plugin1_controller)
    p['ExternalPorts'] = ["9333"]
    assert not verify(p, b.Plugin())


def test_bad_iports():
    p = deepcopy(plugin1_controller)
    p['InternalPorts'] = ["9333"]
    assert not verify(p, b.Plugin())


def test_matched_ports():
    p = deepcopy(plugin1_controller)
    p['ExternalPorts'] = ["9333/tcp"]
    p['InternalPorts'] = ["9333/tcp"]
    assert verify(p, b.Plugin())


def test_mismatched_ports():
    p = deepcopy(plugin1_controller)
    p['ExternalPorts'] = ["9333/tcp"]
    p['InternalPorts'] = ["3339/tcp"]
    assert verify(p, b.Plugin())


def test_bad_length_ports():
    p = deepcopy(plugin1_controller)
    p['ExternalPorts'] = ["9333/tcp"]
    p['InternalPorts'] = ["2400/tcp", "4200/tcp"]
    assert not verify(p, b.Plugin())


def test_bad_length_ports():
    p = deepcopy(plugin1_controller)
    p['ExternalPorts'] = ["9333/tcp", "4200/tcp"]
    p['InternalPorts'] = ["2400/tcp"]
    assert not verify(p, b.Plugin())

def test_no_envs():
    p = deepcopy(plugin1_controller)
    del (p['Environment'])
    assert not verify(p, b.Plugin())


def test_no_value_envs():
    p = deepcopy(plugin1_controller)
    p['Environment'] = ["key="]
    assert not verify(p, b.Plugin())

def test_no_key_envs():
    p = deepcopy(plugin1_controller)
    p['Environment'] = ["=value"]
    assert not verify(p, b.Plugin())


def test_duplicate_keys_overwrite_ok_envs():
    p = deepcopy(plugin1_controller)
    p['Environment'] = ["key1=value", "key1=value2"]
    # should expect env to be set with key1=value2 in this case
    assert verify(p, b.Plugin())
