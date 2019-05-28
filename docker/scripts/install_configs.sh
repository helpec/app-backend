#!/bin/bash

virtualenv -p /usr/bin/python3.6 /opt/site

mv ./docker/confs/default /etc/nginx/sites-available/default 

mkdir -p /var/log/web/
mv ./docker/confs/django.conf /etc/supervisor/conf.d/django.conf

# mysqld_safe --skip-grant-tables
# mysql -uroot -e"""
#     use mysql;
#     update user set authentication_string=PASSWORD("root") where User='root';                                                                                 
#     flush privileges;
# """

/etc/init.d/nginx reload
supervisord 
