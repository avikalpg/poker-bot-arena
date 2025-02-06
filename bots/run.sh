#!/bin/sh
source .venv/bin/activate
export FLASK_APP=main
export FLASK_ENV=development
flask run