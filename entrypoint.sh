#!/bin/bash
set -e  # Exit on error

echo "Running migrations..."
poetry run python manage.py migrate --noinput

echo "Starting Gunicorn..."
poetry run gunicorn baddy.wsgi:application \
    --bind unix:/app/gunicorn.sock \
    --workers 3 --timeout 300 &

# Wait for Gunicorn to create the socket
while [ ! -S /app/gunicorn.sock ]; do
    echo "Waiting for Gunicorn to start..."
    sleep 1
done

echo "Gunicorn is running, starting Nginx ✅"
nginx -g "daemon off;"
