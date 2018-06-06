import docker
import rethinkdb as r
from pytest import fixture
import time as T



CLIENT = docker.from_env()

@fixture(scope="module")
def something():
	CLIENT.containers.run(
		"ramrodpcp/database-brain:dev",
		name="Brain",
		detach=True,
		ports={"28015/tcp": 28015},
		remove=True
	)
	T.sleep(8)
	yield "127.0.0.1"

	containers = CLIENT.containers.list()
	for container in containers:
		if container.name == "Brain": 
			container.stop()
			break

def test_connect(something):
    return r.connect(something).repl()

def test_run_cursor(something):
    cursor = r.db("Brain").table("Targets").changes().run()
    r.db("Brain").table("Targets").insert({"Targets": "Job_Target", "Status": "pending", "Start_Time": int(T.time()), "Job_Command": "Keylogger"}).run()
    for document in cursor: 
        r.db("Audit").table("Targets").insert(document)
        break

def test_audit_contains(something):
    cursor = r.db("Audit").table("Targets").run()
    document = None
    for document in cursor:
         print(document)
    assert document
