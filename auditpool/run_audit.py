from multiprocessing import Pool
from sys import argv, stderr
import rethinkdb as r
from time import sleep


_AUDIT_DB = "AUDIT"
global _CONNECTION_STR
_CONNECTION_STR = "127.0.0.1:28015"
DEBUG = True
_CONTINUE = True



#---------------------------------------------
#---    Modify Below Code

def run_audit(namespace):
    if DEBUG:
        print(namespace)

    #some helpful (and parsed) variables.
    host, port = _CONNECTION_STR.split(":")
    db, table = namespace.split(".")
    conn = r.connect(host, port) #conn object is not thread safe

    # 1. Setup the Change Feed
    # 2. Tail the changefeed
    # 3. For each change coming down the feed
    #       a. Sort out the destination db.table
    #       b. call the add_to_audit function?
    # 4. Catch some rethink exceptions?



    #-----This is just here for an example
    from random import randint
    sleep(randint(1,4))
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

def test_audit_Jobs():
    assert(1==1)

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