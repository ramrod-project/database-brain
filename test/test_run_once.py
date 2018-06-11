from pytest import fixture, raises
import docker
import rethinkdb as r
import time as T

from setup import run_once, remove_placeholder

CLIENT = docker.from_env()

@fixture(scope="module")
def something():
	container_name = "BrainRO"
	CLIENT.containers.run(
		"rethinkdb:2.3.6",
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

def test_plugincreate(something):
	run_once.plugincreate()

def test_placeholdercreate(something):
	run_once.placeholdercreate()

def test_braincreate(something):
	run_once.braincreate()

def test_targetcreate(something):
	run_once.targetcreate()

def test_outputscreate(something):
	run_once.outputscreate()

def test_jobcreate(something):
    run_once.jobcreate()

def test_inserttarget(something):
	r.db("Brain").table("Targets").insert({"Plugin_Name": "Dummy", "Location": "1.1.1.1", "Port": "12345"}).run()

def test_jobsinsert(something):
	r.db("Brain").table("Jobs").insert({"Jobs": "Job_Target", "Status": "pending", "Start_Time": int(T.time()), "Job_Command": "Keylogger"}).run()

def test_outputinsert(something):
	r.db("Brain").table("Outputs").insert({"Job_Entry": "Job_One", "Content": "StringContent"}).run()

def test_cleartarget(something):
	r.db("Brain").table("Targets").delete().run()

def test_clearjobs(something):
	r.db("Brain").table("Jobs").delete().run()

def test_clearoutput(something):
	r.db("Brain").table("Outputs").delete().run()

def test_auditcreate(something):
	run_once.auditcreate()

def test_auditjobcreate(something):
	run_once.auditjobcreate()

def test_remove_placeholder(something):
	try:
		r.db("Plugins").table_create("Placeholder").run()
	except r.errors.ReqlOpFailedError:
		pass
	T.sleep(1)
	remove_placeholder.main()
	T.sleep(1)
	with raises(r.ReqlOpFailedError):
		r.db("Plugins").table("Placeholder").run()