"""Creating db's and tables"""
import rethinkdb as r


def index_create_func(param_db, param_table, param_index):
    """

    :param param_db:
    :param param_table:
    :param param_index:
    :return:
    """
    r.db(param_db).table_create(param_table).run()
    r.db(param_db).table(param_table).index_create(param_index).run()
    r.db(param_db).table(param_table).index_wait(param_index).run()


def connect():
    """
    Connect to the brain
    :return:
    """
    return r.connect("localhost").repl()


def plugincreate():
    """
    Plugins database creation
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
    index_create_func("Brain", "Targets", "PluginName")


def outputscreate():
    """
    Brain.Outputs table creation
    :return:
    """
    # Create table with a nested index
    r.db("Brain").table_create("Outputs").run()
    r.db("Brain").table("Outputs").index_create("Output_jobs", r.row["OutputJob"]["id"]).run()
    r.db("Brain").table("Outputs").index_wait("Output_jobs").run()


def jobcreate():
    """
    Brain.Jobs table creation
    :return:
    """
    index_create_func("Brain", "Jobs", "Status")


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
    Logs table created in the brain database
    :return:
    """
    index_create_func("Brain", "Logs", "rt")


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
