# Helper Project

Backend to Helpec Site in Django and RESTful API 

[![Build Status](https://travis-ci.org/helpec/app-backend.svg?branch=master)](https://travis-ci.org/helpec/app-backend)

[![codecov](https://codecov.io/gh/helpec/app-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/helpec/app-backend)

![Docker Build Status](https://img.shields.io/docker/build/helpec/app-backend.svg)


## Documentação da aplicação
[https://helpec.github.io/app-backend/](https://helpec.github.io/app-backend/)


## Install

```bash
$ pip install -r requirement.txt
$ python manage.py migrate
$ python manage.py runserver
```


# Template em docker-compose 

Cria uma imagem padrão para desenvolvimento e hospedagem de aplicação em Python

## Build image
```sh
$ docker-compose build
```

## Run Docker

### by docker-compose
```sh
$ docker-compose up
```

### by docker run
```sh
$ docker run -ti -p 80:80 -p 8000:8000 docker_img_web:latest /sbin/my_init -- bash -l
```