"""
Pytest file should error if the database is not a brain
"""

from os import environ
from pytest import fixture, raises
import docker

from .brain import connect
from .brain.connection import DefaultConnection, BrainNotReady
CLIENT = docker.from_env()



@fixture(scope='module')
def default_rethink():
    tag = environ.get("TRAVIS_BRANCH", "latest")
    container_name = "brainmoduledefaulttest"
    CLIENT.containers.run(
        "rethinkdb:{}".format(tag),
        name=container_name,
        detach=True,
        ports={"28015/tcp": 28015},
        remove=True
    )
    yield True
    # Teardown for module tests
    containers = CLIENT.containers.list()
    for container in containers:
        if container.name == container_name:
            container.stop()
            break

def test_not_brain_interface(default_rethink):
    with raises(BrainNotReady):
        connect()
