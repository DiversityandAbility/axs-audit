#!/bin/sh
. venv/bin/activate

python run.py "${@:-audit/examples/passport.json}"
