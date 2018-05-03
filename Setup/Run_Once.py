from pytest import raises
import rethinkdb as r
import time as T

def test_connect():
	return r.connect("192.168.43.81", 28015).repl()\

def test_plugincreate():
	return 		r.db_create("Plugins").run()

def test_braincreate():
	return r.db_create("Brain").run()

def test_targetcreate():
	return r.db("Brain").table_create("Targets").run()

def test_outputscreate():
	return r.db("Brain").table_create("Outputs").run()

def test_jobcreate():
	return r.db("Brain").table_create("Jobs").run()

def test_inserttarget():
	return r.db("Brain").table("Targets").insert({"Plugin_Name": "Dummy", "Location": "1.1.1.1", "Port": "12345"}).run()

def test_jobsinsert():
	return r.db("Brain").table("Jobs").insert({"Jobs": "Job_Target", "Status": "pending", "Start_Time": int(T.time()), "Job_Command": "Keylogger"}).run()

def test_outputinsert():
	return r.db("Brain").table("Outputs").insert({"Job_Entry": "Job_One", "Content": "StringContent"}).run()

def test_cleartarget():
	return r.db("Brain").table("Targets").delete().run()

def test_clearjobs():
	return r.db("Brain").table("Jobs").delete().run()

def test_clearoutput():
	return r.db("Brain").table("Outputs").delete().run()

if __name__ == "__main__": 	

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
	assert(1==1)

