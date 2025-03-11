#!/bin/bash
set -o errexit  # Exit immediately if a command exits with a non-zero status
set -o nounset  # Treat unset variables as an error when substituting
set -o pipefail # The return value of a pipeline is the status of the last command to exit with a non-zero status
pip install -r requirements.txt
python manage.py makemigrations 
echo "Made Migrations!!!"
python manage.py migrate
echo "Migrated Successfully!!!"
