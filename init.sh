#!/bin/sh
poetry shell
export FLASK_APP=app/api.py
export FLASK_ENV=development
poetry install
poetry run flask run
