#!/bin/bash

function after_create {
    docker-compose exec mysql_db sh -c """
        mysql -uroot -proot -e 'CREATE DATABASE helpec'
    """
    docker-compose exec webapp sh -c """
            python manage.py makemigrations && \
            python manage.py migrate && \
            python manage.py collectstatic
        """
}
function create_user {
    docker-compose exec webapp sh -c """
        python manage.py createsuperuser
    """
}
