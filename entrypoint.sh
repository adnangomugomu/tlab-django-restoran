#!/bin/bash

wait_for_db() {
  echo "Waiting for database..."
  while ! nc -z mysql8 3306; do
    sleep 1
  done
  echo "Database is ready"
}

wait_for_db

echo "Apply database migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000
