#!/bin/bash
set -e

rethinkdb --daemon --bind all

sleep 1

source /scripts/venv/bin/activate

python3 /scripts/setup/run_once.py

python3 /scripts/auditpool/run_audit.py 127.0.0.1:28015 Brain.Jobs 

while true
do
    sleep 1
done