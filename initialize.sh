#!/bin/bash

virtualenv venv --python=python3

source venv/bin/activate

pip install -r requirements.txt

python3 Setup/Run_Once.py