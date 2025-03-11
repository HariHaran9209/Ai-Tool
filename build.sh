#!/usr/bin/env bash
set -e  # Works in both bash and sh

pip install -r requirements.txt

python manage.py makemigrations 
echo "Made Migrations!!!"

python manage.py migrate
echo "Migrated Successfully!!!"
