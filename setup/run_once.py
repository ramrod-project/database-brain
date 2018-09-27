"""Creating db's and tables"""
import rethinkdb as r


def connect():
    """
    Brain connection
    :return:
    """
    return r.connect("localhost").repl()


def plugincreate():
    """
    Plugins db creation
    :return:
    """
    return r.db_create("Plugins").run()


def placeholdercreate():
    """
    Plugins.Placeholder table creation
    :return:
    """
    return r.db("Plugins").table_create("Placeholder").run()


def braincreate():
    """
    Brain db creation
    :return:
    """
    return r.db_create("Brain").run()


def targetcreate():
    """
    Brain.Targets table creation
    :return:
    """
    return r.db("Brain").table_create("Targets").run()


def outputscreate():
    """
    Brain.Outputs table creation
    :return:
    """
    return r.db("Brain").table_create("Outputs").run()


def jobcreate():
    """
    Brain.Jobs table creation
    :return:
    """
    r.db("Brain").table_create("Jobs").run()
    r.db("Brain").table("Jobs").index_create("Status").run()
    r.db("Brain").table("Jobs").index_wait("Status").run()


def auditcreate():
    """
    Audit db creation
    :return:
    """
    return r.db_create("Audit").run()


def auditjobcreate():
    """
    Audit.Jobs table creation
    :return:
    """
    return r.db("Audit").table_create("Jobs").run()


def audittargetcreate():
    """
    Audit.Targets table creation
    :return:
    """
    return r.db("Audit").table_create("Targets").run()


def controller_create():
    """
    Controller db creation
    :return:
    """
    return r.db_create("Controller").run()


def controller_plugins_create():
    """
    Controller.Plugins table creation
    :return:
    """
    return r.db("Controller").table_create("Plugins").run()


def controller_ports_create():
    """
    Controller.Ports table creation
    :return:
    """
    return r.db("Controller").table_create("Ports").run()


def brainfilescreate():
    """
    Brain.Files table creation
    :return:
    """
    return r.db("Brain").table_create("Files",
                                      primary_key="Name").run()


def brainlogscreate():
    """
    Brain.Logs table creation
    :return:
    """
    r.db("Brain").table_create("Logs").run()
    r.db("Brain").table("Logs").index_create("rt").run()
    r.db("Brain").table("Logs").index_wait("rt").run()


def printdb():
    """
    Printing a list of all databases
    :return:
    """
    print(r.db_list().run())


if __name__ == "__main__":	 # pragma: no cover

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
    brainlogscreate()
    printdb()
    controller_create()
    controller_plugins_create()
    controller_ports_create()

    print("complete")
