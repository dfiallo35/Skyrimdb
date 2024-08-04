#!/bin/bash

# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt

echo "Make Migration..."
python skyrimdb/manage.py makemigrations --noinput
python skyrimdb/manage.py migrate --noinput

echo "Collect Static..."
python skyrimdb/manage.py collectstatic --noinput --clear