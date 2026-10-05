#!/bin/bash
set -e

echo "Running migrations"
python manage.py migrate

echo "Collecting staticfiles"
python manage.py collectstatic --noinput

echo "Starting Granian..."
exec granian --interface wsgi shorty_link.wsgi:application \
    --host 0.0.0.0 \
    --port 8000