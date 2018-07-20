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
		'new_val': {
			'Location': '192.168.1.3',
			'Optional': {
				'init': ''
			},
			'PluginName': 'Harness',
			'Port': '9800',
			'id': '059ed5fc-0263-42b0-962d-7258003fd53a'
		},
		'old_val': None,
		'ts': 15
	}
	sample_job = {
		'new_val': {
			'JobCommand': {
				'CommandName': 'echo',
				'Inputs': [
					{
						'Name': 'EchoString',
						'Tooltip': 'This string will be echoed back',
						'Type': 'textbox', 'Value': 'test'
					}
				],
				'OptionalInputs': [],
				'Output': True,
				'Tooltip': '\nEcho\n\nClient Returns this string verbatim\n\nArguments:\n1. String to Echo\n\nReturns:\nString\n'
			},
			'JobTarget': {
				'Location': '192.168.1.1',
				'PluginName': 'Harness', 'Port': 0
			},
			'StartTime': 0,
			'Status': 'Ready',
			'id': '196a6737-d866-48a4-9a01-ec4d9510d7ab'
		},
		'old_val': None,
		'ts': 15
	}
	run_audit.LOG_DIR = ""
	run_audit.write_log_file("Brain.Targets", sample_target)
	run_audit.write_log_file("Brain.Jobs", sample_job)
	with open("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Targets", run_audit.DAY_STRING), "r") as f:
		for line in f:
			assert "[THU JAN  1 00:00:15 1970]" in line
			assert "(Brain.Targets)" in line
			assert "Location: 192.168.1.3" in line
			assert "Optional: [init: ]" in line
			assert "PluginName: Harness" in line
			assert "Port: 9800" in line
	remove("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Targets", run_audit.DAY_STRING))
	with open("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Jobs", run_audit.DAY_STRING), "r") as f:
		for line in f:
			assert line.replace("\n", "") == "[THU JAN  1 00:00:15 1970] - (Brain.Jobs) ---- JobCommand: [CommandName: echo -- Inputs: [('Name', 'EchoString'): ('Type', 'textbox')] -- OptionalInputs: [] -- Output: True] -- JobTarget: [Location: 192.168.1.1 -- PluginName: Harness -- Port: 0] -- StartTime: 0 -- Status: Ready"
	remove("{}{}.{}.log".format(run_audit.LOG_DIR, "Brain.Jobs", run_audit.DAY_STRING))

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