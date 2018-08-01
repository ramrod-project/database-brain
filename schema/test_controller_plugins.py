from os import environ
from pytest import fixture
from time import sleep
import docker
from .brain import r
from .brain.controller import plugins
CLIENT = docker.from_env()


TEST_PLUGIN_DATA = {
    "Name": "Harness",
    "State": "Available",
    "DesiredState": "",
    "Interface": "",
    "ExternalPorts": ["5000"],
    "InternalPorts": ["5000"]
}

TEST_PORT_DATA = {
    "InterfaceName": "eth0",
    "Address": "192.168.1.1",
    "TCPPorts": ["5000"],
    "UDPPorts": []
}

TEST_PORT_DATA2 = {
    "InterfaceName": "eth0",
    "Address": "192.168.1.1",
    "TCPPorts": ["6000", "7000"],
    "UDPPorts": ["8000"]
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



def test_create_plugin_controller(rethink):
    res = plugins.create_plugin(TEST_PLUGIN_DATA)
    assert isinstance(res, dict)
    assert isinstance(res['generated_keys'], list)
    assert len(res['generated_keys']) == 1

def test_get_plugin_by_name_controller(rethink):
    c = plugins.get_plugin_by_name(TEST_PLUGIN_DATA["Name"])
    assert isinstance(c, r.net.DefaultCursor)
    plugin = c.next()
    del plugin["id"]
    assert plugin == TEST_PLUGIN_DATA

def test_create_port_controller(rethink):
    res = plugins.create_port(TEST_PORT_DATA)
    assert isinstance(res, dict)
    assert isinstance(res['generated_keys'], list)
    assert len(res['generated_keys']) == 1

def test_get_ports_by_ip_controller(rethink):
    c = plugins.get_ports_by_ip(TEST_PORT_DATA["Address"])
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

def test_update_plugin_controller(rethink):
    new_plugin_data = TEST_PLUGIN_DATA
    new_plugin_data["State"] = "Restarting"
    new_plugin_data["DesiredState"] = "Restart"
    res = plugins.update_plugin(new_plugin_data)
    assert isinstance(res, dict)
    assert res["replaced"] == 1
