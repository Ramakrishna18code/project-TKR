#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on error

echo "Installing dependencies..."
pip install -r requirements-render.txt

echo "Setting RENDER environment variable..."
export RENDER=true

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Build completed successfully!"
