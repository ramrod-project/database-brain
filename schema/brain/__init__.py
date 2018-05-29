import rethinkdb
from os import environ
r = rethinkdb



BRAIN_DB = "Brain"
AUDIT_DB = "Audit"
PLUGINDB = "Plugins"
JOBS = "Jobs"
TARGETS = "Targets"
OUTPUTS = "Outputs"
SELF_TEST = {BRAIN_DB: frozenset([JOBS, TARGETS, OUTPUTS]),
             AUDIT_DB: [],
             PLUGINDB: []}

DEFAULT_HOSTS = {"PROD": "rethinkdb",
                 "QA": "rethinkdb",
                 "DEV": "rethinkdb_testing",
                 "TESTING": "localhost",
                 "": "localhost", #environment not configured, try anyway
                 }


class NotReady(Exception):
    pass



def brain_post(connection, requirements=SELF_TEST):
    remote_dbs = [x for x in r.db_list().run(connection)]
    for db in requirements:
        assert (db in remote_dbs), "database {} must exist".format(db)
        remote_tables = frozenset([x for x in r.db(db).table_list().run(connection)])
        for table in requirements[db]:
            assert (table in remote_tables), "{} must exist in {}".format(table, db)

def connect(verify=True,
            auth_key=None,
            user='admin',
            password=None,
            timeout=20,
            ssl=dict(),
            _handshake_version=10,
            **kwargs):
    db = None
    host = DEFAULT_HOSTS.get(environ.get("STAGE"))
    c = r.connect(host, rethinkdb.DEFAULT_PORT,
                  db,
                  auth_key, user, password,
                  timeout,
                  ssl, _handshake_version,
                  **kwargs)
    if verify:
        brain_post(c)
    return c