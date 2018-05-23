#!/bin/bash
# test comment

source venv/bin/activate

rethinkdb --daemon --bind all

sleep 1

python3 ./setup/run_once.py

rethinkdb dump -f db-template.tar.gz