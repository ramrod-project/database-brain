#!/bin/bash
set -e

rethinkdb --daemon --bind all

sleep 1

source /scripts/venv/bin/activate

rethinkdb restore /scripts/db-template.tar.gz

python3 /scripts/setup/remove_placeholder.py

python3 /scripts/auditpool/run_audit.py 127.0.0.1:28015 Brain.Jobs Brain.Targets Controller.Plugins Controller.Ports
