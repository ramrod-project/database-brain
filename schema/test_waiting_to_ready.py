"""
Pytest file for the queries
"""

from os import environ
from pytest import fixture, raises
from time import sleep, time
import docker
from .brain import connect, r
from .brain.connection import DefaultConnection, BrainNotReady
from .brain import queries
from .brain.jobs import WAITING, READY
from .brain.queries.decorators import STATUS_FIELD, START_FIELD
from .brain.queries.writes import insert_jobs, transition_waiting
from brain.queries import RBJ


CLIENT = docker.from_env()


TEST_BASIC_JOB = {STATUS_FIELD: WAITING, START_FIELD:time()}
TEST_FUTURE_JOB = {STATUS_FIELD: WAITING, START_FIELD:time()+6000}


@fixture(scope='module')
def rethink():
    sleep(3) #prior test docker needs to shut down
    tag = environ.get("TRAVIS_BRANCH", "dev").replace("master", "latest")
    container_name = "brainmodule_waiting_change"
    container = CLIENT.containers.run(
        "ramrodpcp/database-brain:{}".format(tag),
        name=container_name,
        detach=True,
        ports={"28015/tcp": 28015},
        remove=True
    )
    yield True
    # Teardown for module tests
    container.stop(timeout=5)


def test_confirm_job_inserted(rethink):
    success = insert_jobs([TEST_BASIC_JOB, TEST_FUTURE_JOB], verify_jobs=False)
    assert success['inserted'] == 2


def test_move_basic_to_ready(rethink):
    success = transition_waiting(time())
    assert success["errors"] == 0
    assert success['replaced'] == 1


def test_insert_basic_again(rethink):
    success = insert_jobs([TEST_BASIC_JOB], verify_jobs=False)
    assert success['inserted'] == 1


def test_third_job_to_ready(rethink):
    success = transition_waiting(time())
    assert success["errors"] == 0
    assert success['replaced'] == 1


def test_transition_with_none_ready(rethink):
    success = transition_waiting(time())
    assert success["errors"] == 0
    assert success['replaced'] == 0


def test_verify_statuses_are_ready(rethink):
    ready_count = 0
    waiting_count = 0
    now_time = time()
    cur = RBJ.run(connect())
    for doc in cur:
        if doc[STATUS_FIELD] == WAITING:
            assert doc[START_FIELD] > now_time
            waiting_count += 1
        else:
            assert doc[START_FIELD] < now_time
            ready_count += 1
    assert ready_count == 2
    assert waiting_count == 1
