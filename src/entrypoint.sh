#!/bin/sh for docker container


python manage.py migrate --no-input
python manage.py collectstatic --no-input

#DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --username admin --email admin@example.ru --noinput

gunicorn config.wsgi:application --bind 0.0.0.0:8000