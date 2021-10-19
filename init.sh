#!/bin/sh
source .venv/bin/activate
export FLASK_APP=./app/api.py
export FLASK_ENV=development
poetry install
flask run
