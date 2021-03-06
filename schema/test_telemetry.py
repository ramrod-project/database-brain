from .test_schema_target import Good_TARGET
from copy import deepcopy
from os import environ
from pytest import fixture, raises
import docker
from time import sleep
from .brain.queries.writes import insert_target
from .brain.telemetry import get_target, get_target_id
from .brain.telemetry import update_common, update_specific, update_telemetry




CLIENT = docker.from_env()
TARGET = deepcopy(Good_TARGET)

@fixture(scope='module')
def rethink():
    sleep(2)
    tag = environ.get("TRAVIS_BRANCH", "dev").replace("master", "latest")
    container_name = "brain_telemetry"
    container = CLIENT.containers.run(
        "ramrodpcp/database-brain:{}".format(tag),
        name=container_name,
        detach=True,
        ports={"28015/tcp": 28015},
        remove=True
    )
    sleep(2)
    yield True
    # Teardown for module tests
    container.stop()


def test_initial_target(rethink):
    insert_target(TARGET, verify_target=True)


def test_update_common(rethink):
    x = TARGET
    tid = get_target_id(x['PluginName'], x["Port"], x['Location'])
    common = {"User": "hello there"}
    assert update_common(tid, common, True).get("replaced") == 1
    tgt = get_target(x['PluginName'], x["Port"], x['Location'])
    assert tgt['Optional']["Common"] == common


def test_update_specific(rethink):
    x = TARGET
    tid = get_target_id(x['PluginName'], x["Port"], x['Location'])
    specific = {"Size": "2 Gallon"}
    assert update_specific(tid, specific).get("replaced") == 1
    tgt = get_target(x['PluginName'], x["Port"], x['Location'])
    assert tgt['Optional']["Specific"] == specific


def test_update_both(rethink):
    x = TARGET
    tid = get_target_id(x['PluginName'], x["Port"], x['Location'])
    common = {"User": "Grandma"}
    specific = {"Size": "Hose"}
    s_o, c_o = update_telemetry(target_id=tid,
                                specific=specific,
                                common=common,
                                verify_telemetry=False)
    assert s_o.get("replaced") == 1
    assert c_o.get("replaced") == 1
    tgt = get_target(x['PluginName'], x["Port"], x['Location'])
    assert tgt['Optional']["Specific"] == specific
    assert tgt['Optional']["Common"] == common

