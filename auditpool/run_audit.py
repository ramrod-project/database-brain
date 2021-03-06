from json import dumps
from multiprocessing import Pool
from sys import argv, stderr
from time import asctime, gmtime, sleep, time

import rethinkdb as r


_AUDIT_DB = "AUDIT"
global _CONNECTION_STR
_CONNECTION_STR = "127.0.0.1:28015"
DEBUG = True
_CONTINUE = True
TS = "ts"
LOG_DIR = "/logs/"
LOG_KEY = "new_val"
DAY_STRING = "_".join(asctime(gmtime(time())).split(" "))

LOGGER_KNOWN_EXCEPTIONS = (AttributeError,
                           KeyError,
                           ValueError,
                           IOError,
                           IndexError,
                           TypeError)


def write_log_file(namespace, document):
    """Writes a line to a log file
    
    Arguments:
        namespace {str} -- namespace of document
        document {dict} -- document to write to the logs
    """
    log_timestamp = asctime(gmtime(document[TS]))
    with open("{}{}.{}.log".format(LOG_DIR, namespace, DAY_STRING), "a") as f:
        log_string = dumps({
            "datetime": log_timestamp.upper(),
            "namespace": namespace,
            "log": document[LOG_KEY]
        })
        f.write("{}\n".format(log_string))


#---------------------------------------------
#---    Modify Below Code
def print_debug_data(printable):
    """
    If debug is set to true, printable will go to stdout
    :param printable: something that can be printed
    :return: None
    """
    if DEBUG:
        print(printable)


def run_audit(namespace):
    print_debug_data(namespace)
    #some helpful (and parsed) variables.
    host, port = _CONNECTION_STR.split(":")
    db, table = namespace.split(".")
    conn = r.connect(host, port) #conn object is not thread safe
    cursor = r.db(db).table(table).changes().run(conn)
    for document in cursor: 
        print_debug_data(document)
        document[TS] = time()
        if not r.db("Audit").table_list().contains(table).run(conn): 
            r.db("Audit").table_create(table).run(conn)
        r.db("Audit").table(table).insert(document).run(conn)
        try:
            write_log_file(namespace, document)
        except LOGGER_KNOWN_EXCEPTIONS as lke:
            stderr.write("LogggerError: {}\n".format(str(lke)))
            stderr.write("\t{}\n".format(namespace))
            stderr.write("\t\t{}\n".format(document))
    #-----this was just here for an example
    return namespace #this allows the function to restart.

def add_to_audit(conn, db, table, document):
    #1. probably a direct insert statement
    raise NotImplementedError

#---  Modify Above Code
#---------------------------------------------


#---------------------------------------------
#---    Create a couple Test cases Below
def test_audit_targets():
    run_audit("Brain.Targets")

#---    Create a couple Test cases Above
#---------------------------------------------



#---------------------------------------------
#---    Special Pool Callback functions,
#---    What is a callback?
def pool_except_callback(ex):
    stderr.write("Uncaught exception, closing:\n")
    stderr.write("%s\n" %(ex))
    pool.terminate()
    global _CONTINUE
    _CONTINUE = False

def pool_done_callback(namespace):
    pool.apply_async(run_audit,
                     [namespace],
                     callback=pool_done_callback,
                     error_callback=pool_except_callback)

# ---Might not want to mess too much with these
# ---------------------------------------------

if __name__ == "__main__":
    if len(argv) < 3:
        stderr.write("Launch the program using\n")
        stderr.write("\t%s <connection> <namespace 1> [<optional ns2> ...]\n" %(argv[0]))
        exit(1)

    _CONNECTION_STR = argv[1]
    namespaces = argv[2:]

    with Pool(processes=len(namespaces)) as pool:
        sleep(1) #allow the pol to setup
        for namespace in namespaces:
            pool.apply_async(run_audit,
                             (namespace, ),
                             callback=pool_done_callback,
                             error_callback=pool_except_callback)
        try:
            while _CONTINUE:
                sleep(1)
        except KeyboardInterrupt:
            stderr.write("interrupted, fin\n")