#!/bin/bash

# Exit immediately if any command fails
set -e

# Run Django migrations to ensure the database is up-to-date
echo "Running migrations..."
poetry run python manage.py migrate --noinput

# Start Gunicorn in the background
echo "Starting Gunicorn..."
poetry run gunicorn baddy.wsgi:application --bind unix:/app/gunicorn.sock --workers 3 --timeout 300 &

# Start Nginx in the foreground (to keep the container running)
echo "Starting Nginx..."
nginx -g "daemon off;"
