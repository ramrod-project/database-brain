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
from .brain.static import STATUS_FIELD, START_FIELD, EXPIRE_FIELD
from .brain.queries.writes import insert_jobs, transition_expired, transition_waiting, expire_filter, status_time_filter
from .brain.queries import RBJ


CLIENT = docker.from_env()

TEST_TIMER_OFFSET = 1200
TEST_TIMER_BIG_OFFSET = 6000
TEST_BASIC_JOB = {STATUS_FIELD: WAITING,
                  START_FIELD: time()-TEST_TIMER_OFFSET,
                  EXPIRE_FIELD: time()+TEST_TIMER_OFFSET}
TEST_NOEXP_JOB = {STATUS_FIELD: WAITING,
                  START_FIELD: time()-TEST_TIMER_OFFSET,
                  EXPIRE_FIELD: time()+TEST_TIMER_OFFSET+TEST_TIMER_BIG_OFFSET}


@fixture(scope='module')
def rethink():
    sleep(3) #prior test docker needs to shut down
    tag = environ.get("TRAVIS_BRANCH", "dev").replace("master", "latest")
    container_name = "brainmodule_expired_change"
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
    success = insert_jobs([TEST_BASIC_JOB, TEST_NOEXP_JOB], verify_jobs=False)
    assert success['inserted'] == 2
    transition_waiting(time())



def test_confirm_job_is_ready(rethink):
    for x in RBJ.run(connect()):
        assert x[STATUS_FIELD] == READY


def test_filter_provides_record(rethink):
    test_now_time = time() + TEST_TIMER_BIG_OFFSET
    need_to_expire = 0
    for x in RBJ.filter(expire_filter(test_now_time)).run(connect()):
        need_to_expire += 1
    assert need_to_expire == 1


def test_confirm_job_can_expire(rethink):
    test_now_time = time() + TEST_TIMER_BIG_OFFSET
    success = transition_expired(test_now_time)
    print(success)
    assert success["errors"] == 0
    assert success['replaced'] == 1

