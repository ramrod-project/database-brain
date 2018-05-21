#!/bin/bash
#
# Install dependencies into virtual env

virtualenv venv --python=python3

source venv/bin/activate

pip install -r requirements.txt