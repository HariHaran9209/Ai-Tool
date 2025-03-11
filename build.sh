#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py makemigrations 
echo "Made Migrations!!!"

python manage.py migrate
echo "Migrated Successfully!!!"
