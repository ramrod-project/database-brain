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
	T.sleep(0.5)
	assert "Plugins" in r.db_list().run()

def test_placeholdercreate(something):
	run_once.placeholdercreate()
	T.sleep(0.5)
	assert "Placeholder" in r.db("Plugins").table_list().run()

def test_braincreate(something):
	run_once.braincreate()
	T.sleep(0.5)
	assert "Brain" in r.db_list().run()

def test_targetcreate(something):
	run_once.targetcreate()
	T.sleep(0.5)
	assert "Targets" in r.db("Brain").table_list().run()

def test_outputscreate(something):
	run_once.outputscreate()
	T.sleep(0.5)
	assert "Outputs" in r.db("Brain").table_list().run()

def test_jobcreate(something):
	run_once.jobcreate()
	T.sleep(0.5)
	assert "Jobs" in r.db("Brain").table_list().run()
	assert "Status" in r.db("Brain").table("Jobs").index_list().run()

def test_inserttarget(something):
	key = r.db("Brain").table("Targets").insert({"Plugin_Name": "Dummy", "Location": "1.1.1.1", "Port": "12345"}).run()["generated_keys"][0]
	T.sleep(0.5)
	assert r.db("Brain").table("Targets").get(key).run() == {"id": key, "Plugin_Name": "Dummy", "Location": "1.1.1.1", "Port": "12345"}

def test_jobsinsert(something):
	t = int(T.time())
	key = r.db("Brain").table("Jobs").insert({"Jobs": "Job_Target", "Status": "pending", "Start_Time": t, "Job_Command": "Keylogger"}).run()["generated_keys"][0]
	T.sleep(0.5)
	assert r.db("Brain").table("Jobs").get(key).run() == {"id": key, "Jobs": "Job_Target", "Status": "pending", "Start_Time": t, "Job_Command": "Keylogger"}

def test_outputinsert(something):
	key = r.db("Brain").table("Outputs").insert({"Job_Entry": "Job_One", "Content": "StringContent"}).run()["generated_keys"][0]
	T.sleep(0.5)
	assert r.db("Brain").table("Outputs").get(key).run() == {"id": key, "Job_Entry": "Job_One", "Content": "StringContent"}

def test_cleartarget(something):
	r.db("Brain").table("Targets").delete().run()

def test_clearjobs(something):
	r.db("Brain").table("Jobs").delete().run()

def test_clearoutput(something):
	r.db("Brain").table("Outputs").delete().run()

def test_auditcreate(something):
	run_once.auditcreate()
	T.sleep(0.5)
	assert "Audit" in r.db_list().run()

def test_auditjobcreate(something):
	run_once.auditjobcreate()
	T.sleep(0.5)
	assert "Jobs" in r.db("Audit").table_list().run()

def test_audittargetcreate(something):
	run_once.audittargetcreate()
	T.sleep(0.5)
	assert "Targets" in r.db("Audit").table_list().run()

def test_controller_create(something):
	run_once.controller_create()
	T.sleep(0.5)
	assert "Controller" in r.db_list().run()

def test_controller_plugins_create(something):
	run_once.controller_plugins_create()
	T.sleep(0.5)
	assert "Plugins" in r.db("Controller").table_list().run()

def test_controller_ports_create(something):
	run_once.controller_ports_create()
	T.sleep(0.5)
	assert "Ports" in r.db("Controller").table_list().run()

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