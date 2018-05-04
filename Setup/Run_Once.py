from pytest import fixture, raises
import docker
import rethinkdb as r
import time as T

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
	return r.connect(something).repl()

def test_plugincreate(something):
	return r.db_create("Plugins").run()

def test_braincreate(something):
	return r.db_create("Brain").run()

def test_targetcreate(something):
	return r.db("Brain").table_create("Targets").run()

def test_outputscreate(something):
	return r.db("Brain").table_create("Outputs").run()

def test_jobcreate(something):
	return r.db("Brain").table_create("Jobs").run()

def test_inserttarget(something):
	return r.db("Brain").table("Targets").insert({"Plugin_Name": "Dummy", "Location": "1.1.1.1", "Port": "12345"}).run()

def test_jobsinsert(something):
	return r.db("Brain").table("Jobs").insert({"Jobs": "Job_Target", "Status": "pending", "Start_Time": int(T.time()), "Job_Command": "Keylogger"}).run()

def test_outputinsert(something):
	return r.db("Brain").table("Outputs").insert({"Job_Entry": "Job_One", "Content": "StringContent"}).run()

def test_cleartarget(something):
	return r.db("Brain").table("Targets").delete().run()

def test_clearjobs(something):
	return r.db("Brain").table("Jobs").delete().run()

def test_clearoutput(something):
	return r.db("Brain").table("Outputs").delete().run()

"""if __name__ == "__main__": 	

	test_connect()
	test_plugincreate()
	test_braincreate()
	test_targetcreate()
	test_outputscreate()
	test_jobcreate()
	test_inserttarget()
	test_jobsinsert()
	test_outputinsert()
	test_cleartarget()
	test_clearjobs()
	test_clearoutput()

	test_A()	
	print("complete")
def test_A():
	assert(1==1)"""