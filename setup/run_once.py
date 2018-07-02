import rethinkdb as r

def connect():
	return r.connect("localhost").repl()

def plugincreate():
	return r.db_create("Plugins").run()

def placeholdercreate():
	return r.db("Plugins").table_create("Placeholder").run()
 
def braincreate():
	return r.db_create("Brain").run()

def targetcreate():
	return r.db("Brain").table_create("Targets").run()

def outputscreate():
	return r.db("Brain").table_create("Outputs").run()

def jobcreate():
	return r.db("Brain").table_create("Jobs").run()

def auditcreate():
	return r.db_create("Audit").run()

def auditjobcreate():
	return r.db("Audit").table_create("Jobs").run()

def audittargetcreate():
	return r.db("Audit").table_create("Targets").run()

def controller_create():
	return r.db_create("Controller").run()

def controller_plugins_create():
	return r.db("Controller").table_create("Plugins").run()

def controller_ports_create():
	return r.db("Controller").table_create("Ports").run()

def brainfilescreate():
	return r.db("Brain").table_create("Files").run()

def printdb():
	print(r.db_list().run())

if __name__ == "__main__":	# pragma: no cover

	connect()
	plugincreate()
	placeholdercreate()
	braincreate()
	targetcreate()
	outputscreate()
	jobcreate()
	auditcreate()
	auditjobcreate()
	audittargetcreate()
	brainfilescreate()
	printdb()
	controller_plugins_create()
	controller_ports_create()

	print("complete")