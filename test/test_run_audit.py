from os import environ, remove
import time as T

import docker
import rethinkdb as r
from pytest import fixture

from auditpool import run_audit


CLIENT = docker.from_env()

@fixture(scope="module")
def something():
	try:
		tag = environ.get("TRAVIS_BRANCH", "dev").replace("master", "latest")
	except KeyError:
		tag = "latest"
	CLIENT.containers.run(
		"".join(("ramrodpcp/database-brain:", tag)),
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

def test_format_list():
	"""Test the fomat_list function
	"""
	test_list = [("string", "tuple"), (1, 2), ("dict", {"key1": "value1"})]
	result = run_audit.format_list(test_list)
	assert isinstance(result, str)
	assert result == "[string: tuple -- 1: 2 -- dict: {'key1': 'value1'}]"

def test_format_dictionary():
	"""Test the format_dictionary function
	"""
	test_dict = {"key1": "value1", "key2": 2, "key3": {"subkey1": "subvalue1", 3: 3}}
	result = run_audit.format_dictionary(test_dict)
	assert isinstance(result, list)
	assert result == [('key1', 'value1'), ('key2', 2), ('key3', [('subkey1', 'subvalue1'), (3, 3)])]

def test_write_log_file():
	"""Test writing to a log file
	"""
	sample_target = {
		"id": "w93hyh-vc83j5i-v82h54u-b6eu4n",
		"PluginName": "IntegrationTest",
		"Location": "127.0.0.1",
		"Port": "8080",
		"Optional": {
			"TestVal1": "Test value",
			"TestVal2": "Test value 2"
		},
		"ts": 1529424989.6637425
	}
	sample_job = {
		"id": "138thg-eg98198-sf98gy3-feh8h8",
		"JobTarget": sample_target,
		"Status": "Ready",
		"StartTime": 1529424989.6637425,
		"JobCommand": "Do stuff",
		"ts": 1529424989.6637425
	}
	run_audit.LOG_DIR = ""
	run_audit.write_log_file("Brain.Jobs", sample_job)
	run_audit.write_log_file("Brain.Targets", sample_target)
	with open("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Jobs", run_audit.DAY_STRING), "r") as f:
		for line in f:
			print(line)
			assert line == "[TUE JUN 19 16:16:29 2018] - (Brain.Jobs) ---- JobTarget: [PluginName: IntegrationTest -- Location: 127.0.0.1 -- Port: 8080 -- Optional: [TestVal1: Test value -- TestVal2: Test value 2] -- ts: 1529424989.6637425] -- Status: Ready -- StartTime: 1529424989.6637425 -- JobCommand: Do stuff -- ts: 1529424989.6637425\n"
	remove("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Jobs", run_audit.DAY_STRING))
	with open("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Targets", run_audit.DAY_STRING), "r") as f:
		for line in f:
			print(line)
			assert line == "[TUE JUN 19 16:16:29 2018] - (Brain.Targets) ---- PluginName: IntegrationTest -- Location: 127.0.0.1 -- Port: 8080 -- Optional: [TestVal1: Test value -- TestVal2: Test value 2] -- ts: 1529424989.6637425\n"
	remove("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Targets", run_audit.DAY_STRING))

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