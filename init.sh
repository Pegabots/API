#!/bin/sh
source venv/bin/activate
export FLASK_APP=./app/api.py
export FLASK_ENV=development
pip install -r ./requirements.txt
flask run
