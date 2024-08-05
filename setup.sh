#!/bin/bash

# Build the project
echo "Building the project..."
pip install setuptools
pip install -r requirements.txt

echo "Make Migration..."
python3.9 skyrimdb/manage.py makemigrations
python3.9 skyrimdb/manage.py migrate
