import rethinkdb as r
from pytest import fixture, raises
from setup import run_once
from time import sleep
import docker
from os import environ
CLIENT = docker.from_env()

@fixture(scope="module")
def rethink():
    try:
        tag = environ.get("TRAVIS_BRANCH", "dev").replace("master", "latest")
    except KeyError:
        tag = "latest"
    CLIENT.containers.run(
        "".join(("ramrodpcp/database-brain:", tag)),
        name="rethinkdb",
        detach=True,
        ports={"28015/tcp":28015},
        remove=True
    )
    sleep(3)
    yield r.connect("127.0.0.1", 28015)
    try:
        environ["LOGLEVEL"]=""
        containers = CLIENT.containers.list()
        for container in containers:
            if container.name == "rethinkdb":
                container.stop()
                break
    except SystemExit:
        pass

def test_brain(rethink):  
    r.db_list().contains("Brain").run(rethink)

def test_plugins(rethink):  
    r.db_list().contains("Plugins").run(rethink)

def test_brain_targets(rethink):
    r.db("Brain").table("Targets").run(rethink)

def test_brain_output(rethink):  
    r.db("Brain").table("Outputs").run(rethink)

def test_brain_jobs(rethink):   
    r.db("Brain").table("Jobs").run(rethink)

def test_audit(rethink):
    r.db_list().contains("Audit").run(rethink)

def test_audit_jobs(rethink):    
    r.db("Audit").table("Jobs").run(rethink)

def test_brain_files(rethink):
    r.db("Brain").table("Files").run(rethink)