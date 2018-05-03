import rethinkdb as r
import time as T

if __name__ == "__main__": 

	try:
		r.connect("192.168.43.81", 28015).repl()
	except Exception as Ex:
		print(Ex)

	try:
		r.db_create("Plugins").run()
		
	except Exception as Ex:
		print (Ex)
		
	try:
		r.db_create("Brain").run()
		r.db("Brain").table_create("Targets").run()
		r.db("Brain").table_create("Outputs").run()
	except Exception as Ex:
		print (Ex)

	try:
		r.db("Brain").table_create("Jobs").run()
	except Exception as Ex:
		print (Ex)

	try:
		r.db("Brain").table("Targets").insert({"Plugin_Name": "Dummy", "Location": "1.1.1.1", "Port": "12345"}).run()
	except Exception as Ex:
		print (Ex)
		
	try:
		r.db("Brain").table("Jobs").insert({"Jobs": "Job_Target", "Status": "pending", "Start_Time": int(T.time()), "Job_Command": "Keylogger"}).run()
	except Exception as Ex:
		print (Ex)
		
	try:
		r.db("Brain").table("Outputs").insert({"Job_Entry": "Job_One", "Content": "StringContent"}).run()
	except Exception as Ex:
		print (Ex)
		
	test_A()	
	print("complete")
def test_A():
	assert(1==1)

