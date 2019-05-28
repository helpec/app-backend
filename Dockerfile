FROM phusion/baseimage:0.10.0

ADD ./ /code
WORKDIR /code

RUN ./docker/scripts/install_libs.sh
RUN ./docker/scripts/install_configs.sh

RUN mkdir -p /opt/site/app &&\
    cp -a /code /opt/site/app &&\
    rm -r /code 

WORKDIR /opt/site/app

RUN ../bin/pip install -r requirements.txt &&\
    ../bin/python ./manage.py makemigration &&\
    ../bin/python ./manage.py migrate &&\
    ../bin/python ./manage.py collectstatic


CMD ["/sbin/my_init -- bash -l"]