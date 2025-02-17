#!/bin/bash

# Exit immediately if any command fails
set -e

# Run Django migrations to ensure the database is up-to-date
echo "Running migrations..."
poetry run python manage.py migrate --noinput

# Start Nginx
echo "Starting Nginx..."
service nginx start

# Start the Gunicorn server
echo "Starting Gunicorn..."
poetry run gunicorn --bind 0.0.0.0:8000 baddy.wsgi:application
