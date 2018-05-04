from pytest import fixture, raises
import docker
import rethinkdb as r
import time as T

from setup import run_once

CLIENT = docker.from_env()

@fixture(scope="module")
def something():
	CLIENT.containers.run(
		"rethinkdb",
		name="Brain",
		detach=True,
		ports={"28015/tcp": 28015},
		remove=True
	)
	T.sleep(1)
	yield "127.0.0.1"

	containers = CLIENT.containers.list()
	for container in containers:
		if container.name == "Brain": 
			container.stop()
			break


def test_connect(something):
	run_once.connect()

def test_plugincreate(something):
	run_once.plugincreate()

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
	return r.db("Brain").table("Targets").delete().run()

def test_clearjobs(something):
	return r.db("Brain").table("Jobs").delete().run()

def test_clearoutput(something):
	return r.db("Brain").table("Outputs").delete().run()