import rethinkdb as r

def main():
    r.connect().repl()
    r.db("Plugins").table_drop("Placeholder").run()

if __name__ == '__main__':
    main()