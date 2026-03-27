#!/usr/bin/env bash
# Wyjście z błędem, jeśli jakakolwiek komenda zawiedzie
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate