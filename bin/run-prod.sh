#!/bin/sh

./bin/run-common.sh
gunicorn accountable.wsgi:application -b 0.0.0.0:${PORT:-8000} --log-file -
