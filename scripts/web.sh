#!/bin/sh
. venv/bin/activate

flask --app audit.web.main run --debug
