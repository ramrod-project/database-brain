import rethinkdb as r


def connect():
	return r.connect("127.0.0.1").repl()

def plugincreate():
	return r.db_create("Plugins").run()

def braincreate():
	return r.db_create("Brain").run()

def targetcreate():
	return r.db("Brain").table_create("Targets").run()

def outputscreate():
	return r.db("Brain").table_create("Outputs").run()

def jobcreate():
	return r.db("Brain").table_create("Jobs").run()

if __name__ == "__main__": 	

	connect()
	plugincreate()
	braincreate()
	targetcreate()
	outputscreate()
	jobcreate()

	print("complete")