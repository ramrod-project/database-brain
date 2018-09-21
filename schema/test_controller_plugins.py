from os import environ
from copy import deepcopy
from pytest import fixture, raises
from time import sleep
from time import time
import docker
from .brain import r
from .brain.controller import plugins
CLIENT = docker.from_env()


HARNESS_ID = "111-AAA"
HARNESS_NAME = "Harness"

TEST_PLUGIN_DATA = {
    "id": HARNESS_ID,  # prod systems should allow auto-generated IDs
    "Name": HARNESS_NAME,
    "ServiceName": "{}-5000tcp".format(HARNESS_NAME),
    "State": "Available",
    "OS": "posix",
    "DesiredState": "",
    "Interface": "192.168.1.1",
    "Environment": ["STAGE=DEV", "NORMAL=1"],
    "ExternalPorts": ["5000/tcp"],
    "InternalPorts": ["5000/tcp"]
}


TEST_PROD_PLUGIN_DATA = {
    "Name": "AnotherThing",
    "ServiceName": "AnotherThing-5600tcp",
    "State": "Available",
    "DesiredState": "",
    "OS": "posix",
    "Interface": "",
    "Environment": ["STAGE=DEV", "NORMAL=1"],
    "ExternalPorts": ["5600/tcp"],
    "InternalPorts": ["5600/tcp"]
}


TEST_PORT_DATA = {
    "InterfaceName": "eth0",
    "Interface": "192.168.1.1",
    "NodeHostName": "home",
    "OS": "posix",
    "TCPPorts": ["5000"],
    "UDPPorts": []
}

TEST_PORT_DATA2 = {
    "InterfaceName": "eth0",
    "Interface": "192.168.1.1",
    "NodeHostName": "home",
    "OS": "posix",
    "TCPPorts": ["6000", "7000"],
    "UDPPorts": ["8000"]
}

TEST_TARGET = {"PluginName":"TestPlugin",
               "Location": "192.168.1.1",
               "Port": "0",
               "Optional": "example"}

TEST_CAPABILITY = [
    {
        "CommandName": "echo",
        "Tooltip": "",
        "Output": True,
        "Inputs": [
                {"Name": "EchoString",
                 "Type": "textbox",
                 "Tooltip": "This string will be echoed back",
                 "Value": ""
                 },
                ],
        "OptionalInputs": []
    }
]

TEST_JOB = {
    "JobTarget": TEST_TARGET,
    "Status": "Ready",
    "StartTime": 7,
    "JobCommand": TEST_CAPABILITY[0]
}

@fixture(scope='module')
def rethink():
    sleep(3) #prior test docker needs to shut down
    tag = environ.get("TRAVIS_BRANCH", "dev").replace("master", "latest")
    container_name = "brainmodule_controller_test"
    container = CLIENT.containers.run(
        "ramrodpcp/database-brain:{}".format(tag),
        name=container_name,
        detach=True,
        ports={"28015/tcp": 28015},
        remove=True
    )
    yield True
    # Teardown for module tests
    container.stop()


def test_create_harness_plugin_controller(rethink):
    res = plugins.create_plugin(TEST_PLUGIN_DATA)
    assert isinstance(res, dict)
    assert res['inserted'] == 1


def test_get_harness_plugin_controller(rethink):
    res = plugins.get(HARNESS_ID)
    assert isinstance(res, dict)
    assert res['id'] == HARNESS_ID
    assert res == TEST_PLUGIN_DATA


def test_create_plugin_controller(rethink):
    res = plugins.create_plugin(TEST_PROD_PLUGIN_DATA)
    assert isinstance(res, dict)
    assert isinstance(res['generated_keys'], list)
    assert len(res['generated_keys']) == 1


def test_create_plugin_controller(rethink):
    test_copy = deepcopy(TEST_PROD_PLUGIN_DATA)
    test_copy["ServiceName"] = "Any_Uniqie_SN"
    res = plugins.create_plugin(test_copy)
    assert isinstance(res, dict)
    assert isinstance(res['generated_keys'], list)
    assert len(res['generated_keys']) == 1


def test_get_names(rethink):
    res = plugins.get_names()
    assert len(res) == 2
    assert TEST_PLUGIN_DATA['Name'] in res
    assert TEST_PROD_PLUGIN_DATA['Name'] in res


def test_get_plugin_by_name_controller(rethink):
    c = plugins.get_plugin_by_name(TEST_PLUGIN_DATA["Name"])
    assert isinstance(c, r.net.DefaultCursor)
    plugin = c.next()
    assert plugin == TEST_PLUGIN_DATA


def test_create_port_controller(rethink):
    res = plugins.create_port(TEST_PORT_DATA)
    assert isinstance(res, dict)
    assert isinstance(res['generated_keys'], list)
    assert len(res['generated_keys']) == 1


def test_get_ports_by_ip_controller(rethink):
    c = plugins.get_ports_by_ip(TEST_PORT_DATA["Interface"])
    assert isinstance(c, r.net.DefaultCursor)
    port_entry = c.next()
    del port_entry["id"]
    assert port_entry == TEST_PORT_DATA


def test_create_update_port_controller(rethink):
    res = plugins.create_port(TEST_PORT_DATA2)
    print(res)
    assert isinstance(res, dict)
    assert res['replaced'] == 1


def test_check_port_conflict(rethink):
    res = plugins.create_port(TEST_PORT_DATA)
    assert isinstance(res, dict)
    assert res["errors"] == 1


def test_update_plugin_controller_with_id(rethink):
    new_plugin_data = TEST_PLUGIN_DATA
    new_plugin_data["State"] = "Restarting"
    new_plugin_data["DesiredState"] = "Restart"
    res = plugins.update_plugin(new_plugin_data)
    assert isinstance(res, dict)
    assert res["replaced"] == 1


def test_update_plugin_controller_with_ServiceName(rethink):
    from copy import deepcopy
    new_plugin_data = deepcopy(TEST_PLUGIN_DATA)
    del new_plugin_data['id']
    new_plugin_data["State"] = "Stop"
    new_plugin_data["DesiredState"] = "Activate"
    res = plugins.update_plugin(new_plugin_data)
    assert isinstance(res, dict)
    assert res["replaced"] == 1

def test_update_plugin_controller_fail_DS(rethink):
    from copy import deepcopy
    new_plugin_data = deepcopy(TEST_PLUGIN_DATA)
    del new_plugin_data['id']
    new_plugin_data["DesiredState"] = False
    with raises(ValueError):
        res = plugins.update_plugin(new_plugin_data, verify_plugin=True)
    assert plugins.get(TEST_PLUGIN_DATA["id"])["DesiredState"] is not False

def test_update_plugin_controller_fail_EP(rethink):
    from copy import deepcopy
    new_plugin_data = deepcopy(TEST_PLUGIN_DATA)
    del new_plugin_data['id']
    new_plugin_data["ExternalPorts"].append("3000/tcp")
    with raises(ValueError):
        res = plugins.update_plugin(new_plugin_data, verify_plugin=True)
    assert len(plugins.get(TEST_PLUGIN_DATA["id"])["ExternalPorts"] ) == 1

def test_update_plugin_controller_fail_ENV(rethink):
    from copy import deepcopy
    new_plugin_data = deepcopy(TEST_PLUGIN_DATA)
    del new_plugin_data['id']
    new_plugin_data["Environment"].append("NoValue=")
    with raises(ValueError):
        res = plugins.update_plugin(new_plugin_data, verify_plugin=True)
    assert len(plugins.get(TEST_PLUGIN_DATA["id"])["Environment"]) == 2


def test_update_plugin_active(rethink):
    plugins.activate(HARNESS_ID)
    cur = [x for x in plugins.get_plugin_by_name(HARNESS_NAME)]
    assert len(cur) == 1
    assert cur[0]["DesiredState"] == "Activate"


def test_update_plugin_restart(rethink):
    plugins.restart(HARNESS_ID)
    cur = [x for x in plugins.get_plugin_by_name(HARNESS_NAME)]
    assert len(cur) == 1
    assert cur[0]["DesiredState"] == "Restart"
    assert isinstance(cur[0]["Environment"], list)
    _k0, _v0 = cur[0]["Environment"][0].split("=")
    assert _v0 == "restart"
    assert int(_k0) <= int(time())


def test_update_plugin_stop(rethink):
    plugins.stop(HARNESS_ID)
    cur = [x for x in plugins.get_plugin_by_name(HARNESS_NAME)]
    assert len(cur) == 1
    assert cur[0]["DesiredState"] == "Stop"


def test_get_interfaces(rethink):
    res = plugins.get_interfaces()
    assert len(res) == 1
    assert TEST_PORT_DATA['Interface'] in res
    assert TEST_PORT_DATA2['Interface'] in res

def test_record_state(rethink):
    state = {"192.168.1.1": TEST_JOB}
    plugins.record_state(TEST_PLUGIN_DATA["ServiceName"], state, r.connect())
    res = plugins.get(TEST_PLUGIN_DATA["id"])
    assert res["PluginState"] == state

def test_recover_state(rethink):
    state = plugins.recover_state(TEST_PLUGIN_DATA["ServiceName"], r.connect())
    assert state["192.168.1.1"] == TEST_JOB
    
