#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Ta linijka uruchomi nasz skrypt tworzenia admina:
python create_admin.py