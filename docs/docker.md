# Instalar em Ambiente Docker

# Template em docker-compose 

Cria uma imagem padrão para desenvolvimento e hospedagem de aplicação em Python

## Build image
```sh
$ docker-compose build
```

## Run Docker

* ### by docker-compose
    ```sh
    $ docker-compose up
    ```

* ### by docker run
    ```sh
    $ docker run -ti -p 80:80 -p 8000:8000 docker_img_web:latest /sbin/my_init -- bash -l
    ```