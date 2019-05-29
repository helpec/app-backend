# Instalar o Ambiente Local


## Docker MYSQL DEV

```bash
docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8
```

## Criar o virtualenv

```bash
$ virtualenv -p /usr/bin/python3.6 app_backend
```

## Clonar o código fonte da aplicação

```bash
$ cd app_backend
$ git clone https://github.com/helpec/app-helpec app 
```

## Instalar as dependências do python

```bash
$ cd app
$ ../bin/pip install -r requirements.txt 
```

## Criar o banco de dados e o usuário root da aplicação

```bash
$ ../bin/python ./manage.py makemigration
$ ../bin/python ./manage.py migrate
$ ../bin/python ./manage.py createsuperuser
```

## Coletar arquivos estaticos da aplicação

```bash
$ ../bin/python ./manage.py collectstatic
````

## Executar o servidor de desenvolvimento

```bash
$ ../bin/python ./manage.py runserver 
```

## Acessar no seu navegador a URL

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## API para desenvolvimento

### Postman

Coleção destinada a utilização manual e desenvolvimento da API 

* [Documentação Online](https://documenter.getpostman.com/view/1391125/S1EQSxoL0)
* [Colection para importação](https://www.getpostman.com/collections/2bfa6338edcaeed4f607)


### Environment Variables

Crie um `environment` no postman com os parametros abaixo:

|Key|Value|
|---|---|
|token|XXXXXX|
|apiUrl|https://api.helpec.com.br|
