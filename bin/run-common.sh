#!/bin/bash

./manage.py migrate
yes yes | ./manage.py collectstatic
