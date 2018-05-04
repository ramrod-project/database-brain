#!/bin/bash
set -e

rethinkdb --daemon --bind all

sleep 1

source /scripts/venv/bin/activate

python3 /scripts/setup/run_once.py

while true
do
    sleep 1
done