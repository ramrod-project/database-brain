#!/bin/bash
set -e

sleep 1

source /scripts/venv/bin/activate

rethinkdb restore /scripts/db-template.tar.gz

python3 /scripts/setup/remove_placeholder.py

