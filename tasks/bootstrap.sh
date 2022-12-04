#!/bin/sh
# ---
# help-text: Bootstrap this project
# ---
set -eu

python3.10 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install