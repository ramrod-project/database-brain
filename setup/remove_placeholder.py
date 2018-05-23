import rethinkdb as r

if __name__ == '__main__':
    r.connect().repl()
    r.db("Plugins").table_drop("Placeholder").run()