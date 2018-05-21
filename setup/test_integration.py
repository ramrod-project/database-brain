import rethinkdb as r
from pytest import fixture, raises
from setup import run_once
import docker
from os import environ

@fixture(scope="module")
def rethink():
    try:
        tag=environ["TRAVIS_BRANCH"]
    except KeyError:
        tag="latest"
    CLIENT.containers.run("".join("ramrodpcp/database-brain:",tag), name="rethinkdb", detach=True, ports={"28015/tcp":28015}, remove=True)
    sleep(8)
    yield
    try:
        environ["LOGLEVEL"]=""
        CLIENT.containers.list()
        for container in containers:
            if container.name == "rethinkdb":
                container.stop()
                break
    except SystemExit:
        pass

def test_connect(rethink):
    with raises(ConnectionError):
        r.connect("", 28015).repl()

def test_connect_good(rethink):
    good = r.connect("127.0.0.1", 28015).repl()
    assert isinstance(good, r.Connection)

def test_brain(rethink):
    r.db_list().contains('Brain')

def test_plugins(rethink):
    r.db_list().contains('Plugins')

def test_brain_targets(rethink):
    r.db("Brain").contains('Targets')

def test_brain_output(rethink):
    r.db("Brain").contains('Outputs')

def test_brain_jobs(rethink):
    r.db("Brain").contains('Jobs')

def test_audit(rethink):
    r.db_list().contains('Audit')

def test_audit_jobs(rethink):
    r.db("Audit").contains('Jobs')
