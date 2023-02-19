#!/bin/sh
chmod +x entrypoint.sh


if [ "$DATABASE" = "strip_project_1_db" ]
then
    echo "Waiting for strip_project_1_db..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
# python manage.py runserver

exec "$@"

