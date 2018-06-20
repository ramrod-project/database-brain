from multiprocessing import Pool
from sys import argv, stderr
from time import asctime, gmtime, sleep, time

import rethinkdb as r
from jinja2 import Template


_AUDIT_DB = "AUDIT"
global _CONNECTION_STR
_CONNECTION_STR = "127.0.0.1:28015"
DEBUG = True
_CONTINUE = True
TS = "ts"
LOG_DIR = "/logs/"
LOG_KEY = "new_val"
DAY_STRING = "_".join((
    asctime(gmtime(time())).split(" ")[1],
    asctime(gmtime(time())).split(" ")[2],
    asctime(gmtime(time())).split(" ")[4]
))
_LOG_TEMPLATE = Template(
    """[{{ date_string }}] - ({{ namespace_string }}) ---- {{ other_stuff }}"""
)

LOGGER_KNOWN_EXCEPTIONS = (AttributeError,
                           KeyError,
                           ValueError,
                           IOError)

def format_list(input_list):
    """Formats lists for rendering

    Takes format_dictionary output list of tuples
    and formats it for nicer printing. Calls recursively
    for lists in each tuple.
    
    Arguments:
        input {list[tuple]} -- list of tuples.
    
    Returns:
        {str} -- printable string based on list
    """
    pre_format_list = []
    for item in input_list:
        if isinstance(item[1], list):
            pre_format_list.append("{}: {}".format(item[0], format_list(item[1])))
        else:
            pre_format_list.append("{}: {}".format(item[0], item[1]))
    return "[{}]".format(" -- ".join(pre_format_list))


def format_dictionary(input_dict):
    """Return a dictionary as a list of tuples
    
    Takes a dictionary and returns a list of tuples
    (key, value). Calls recursively when type(value)
    is dict.
    
    Arguments:
        input {dict} -- dictionary.
    
    Returns:
        {list} -- list of tuples (key, value)
    """
    formatted_list = []
    for key, value in input_dict.items():
        if key == "ts" or key == "id" or key == "Tooltip":
            continue
        elif isinstance(value, list):
            formatted_list.append((key, [format_dictionary(val) for val in value]))
        elif isinstance(value, dict):
            formatted_list.append((key, format_dictionary(value)))
        else:
            formatted_list.append((key, value))
    return formatted_list


def write_log_file(namespace, document):
    """Writes a line to a log file
    
    Arguments:
        namespace {str} -- namespace of document
        document {dict} -- document to write to the logs
    """
    log_timestamp = asctime(gmtime(document[TS]))
    with open("{}{}.{}.log".format(LOG_DIR, namespace, DAY_STRING), "a") as f:
        log_string = _LOG_TEMPLATE.render(
            date_string=log_timestamp.upper(),
            namespace_string=namespace,
            other_stuff=format_list(format_dictionary(document[LOG_KEY]))[1:-1]
        )
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