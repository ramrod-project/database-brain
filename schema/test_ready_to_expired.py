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
from .brain.jobs import WAITING, READY, ERROR, PENDING, DONE
from .brain.static import STATUS_FIELD, START_FIELD, EXPIRE_FIELD, ID_FIELD, TIMEOUT_ERROR
from .brain.queries.writes import insert_jobs, transition_expired, transition_waiting, expire_filter
from .brain.queries import RBJ, get_output_content


CLIENT = docker.from_env()

TEST_TIMER_OFFSET = 1200
TEST_TIMER_BIG_OFFSET = 6000
TEST_BASIC_JOB = {STATUS_FIELD: WAITING,
                  START_FIELD: time()-TEST_TIMER_OFFSET,
                  EXPIRE_FIELD: time()+TEST_TIMER_OFFSET}
TEST_PENDX_JOB = {STATUS_FIELD: PENDING,
                  START_FIELD: time()-TEST_TIMER_OFFSET,
                  EXPIRE_FIELD: time()+TEST_TIMER_OFFSET}
TEST_DONEX_JOB = {STATUS_FIELD: DONE,
                  START_FIELD: time()-TEST_TIMER_OFFSET-TEST_TIMER_BIG_OFFSET,
                  EXPIRE_FIELD: time()-TEST_TIMER_OFFSET}
TEST_NOEXP_JOB = {STATUS_FIELD: WAITING,
                  START_FIELD: time()-TEST_TIMER_OFFSET,
                  EXPIRE_FIELD: time()+TEST_TIMER_OFFSET+TEST_TIMER_BIG_OFFSET}
TEST_WAITX_JOB = {STATUS_FIELD: WAITING,
                  START_FIELD: time()+TEST_TIMER_OFFSET,
                  EXPIRE_FIELD: time()+TEST_TIMER_BIG_OFFSET}

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
    success = insert_jobs([TEST_BASIC_JOB,
                           TEST_PENDX_JOB,
                           TEST_NOEXP_JOB,
                           TEST_WAITX_JOB,
                           TEST_DONEX_JOB],
                          verify_jobs=False)
    assert success['inserted'] == 5
    transition_waiting(time())



def test_confirm_job_is_ready(rethink):
    for x in RBJ.run(connect()):
        if x[START_FIELD] <=  time():
            assert x[STATUS_FIELD] == READY or x[STATUS_FIELD] == PENDING or x[STATUS_FIELD] == DONE
        else:
            assert x[STATUS_FIELD] == WAITING


def test_filter_provides_record(rethink):
    test_now_time = time() + TEST_TIMER_BIG_OFFSET
    need_to_expire = 0
    for x in RBJ.filter(expire_filter(test_now_time)).run(connect()):
        need_to_expire += 1
    assert need_to_expire == 2


def test_confirm_job_can_expire(rethink):
    test_now_time = time() + TEST_TIMER_BIG_OFFSET
    success = transition_expired(test_now_time)
    print(success)
    assert success["errors"] == 0
    assert success['replaced'] == 2


def test_confirm_job_is_expired(rethink):
    expired = 0
    ready = 0
    pending = 0
    done = 0
    for x in RBJ.run(connect()):
        print (x)
        if x[STATUS_FIELD] == ERROR:
            expired += 1
        elif x[STATUS_FIELD] == PENDING:
            pending += 1
        elif x[STATUS_FIELD] == READY:
            ready += 1
        elif x[STATUS_FIELD] == DONE:
            done += 1
    assert expired == 2
    assert ready == 1
    assert pending == 1
    assert done == 1


def test_confirm_timeout_message_set_in_output(rethink):
    expired = 0
    for x in RBJ.filter({STATUS_FIELD: ERROR}).run(connect()):
        expired += 1
        output = get_output_content(x[ID_FIELD])
        assert output == TIMEOUT_ERROR
    assert expired == 2
