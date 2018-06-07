from os import environ
import time as T

import docker
import rethinkdb as r
from pytest import fixture


CLIENT = docker.from_env()

@fixture(scope="module")
def something():
	container_name = "BrainAudit"
	tag = ":latest"
	try:
		if environ["TRAVIS_BRANCH"] == "dev":
			tag = ":dev"
		elif environ["TRAVIS_BRANCH"] == "qa":
			tag = ":qa"
	except KeyError:
		pass
	CLIENT.containers.run(
		"".join(("ramrodpcp/database-brain", tag)),
		name=container_name,
		detach=True,
		ports={"28015/tcp": 28015},
		remove=True
	)
	T.sleep(8)
	yield "127.0.0.1"

	containers = CLIENT.containers.list()
	for container in containers:
		if container.name == container_name:
			container.stop()
			break

def test_connect(something):
    return r.connect(something).repl()

def test_run_cursor(something):
    cursor = r.db("Brain").table("Jobs").changes().run()
    r.db("Brain").table("Jobs").insert({"Jobs": "Job_Target", "Status": "pending", "Start_Time": int(T.time()), "Job_Command": "Keylogger"}).run()
    for document in cursor: 
        r.db("Audit").table("Jobs").insert(document)
        break

def test_audit_contains(something):
    cursor = r.db("Audit").table("Jobs").run()
    for document in cursor:
         print(document)