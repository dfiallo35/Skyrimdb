#!/bin/bash

# Build the project
echo "Building the project..."
pip install setuptools
pip install -r requirements.txt

echo "Make Migration..."
python3.12 manage.py makemigrations
python3.12 manage.py migrate

echo "Collect Static..."
python3.12 manage.py collectstatic
