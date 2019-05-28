#!/bin/bash

apt-get update && apt-get upgrade
apt-get install mysql-server nginx net-tools \
    python3-pip python3-dev python3-setuptools build-essential git libxml2 libxslt1.1 gcc \
    libffi-dev libssl-dev openssl mysql-client libmysqlclient-dev libxml2-dev libxslt1-dev zlib1g-dev \
    python-virtualenv supervisor -y

mkdir -p /var/run/mysqld/ && \
    chown mysql:mysql /var/run/mysqld/

mkdir -p /etc/service/mysqld && \
    mv ./docker/confs/run_mysql /etc/service/mysqld/run && \
    chmod +x /etc/service/mysqld/run

mkdir -p /etc/service/nginx && \
    mv ./docker/confs/run_nginx /etc/service/nginx/run && \
    chmod +x /etc/service/nginx/run

mv ./docker/confs/init_d_supervisor /etc/my_init.d/01_supervisord.sh && \
    chmod +x /etc/my_init.d/01_supervisord.sh
