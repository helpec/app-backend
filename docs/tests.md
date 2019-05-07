# Teste da aplicação

## Instalar dependencias para os testes

```bash
$ cd /path/to/env/app_backend/app
$ ../bin/pip install pylint flake8 coverage black
```

## Executar unittest

```bash
$ cd /path/to/env/app_backend/app
$ python manage.py test -v 2
```

## Analisar o código pelo pylint

```bash
$ cd /path/to/env/app_backend/app
$ ../bin/pylint app_backend/*
```

## Analisar o código pelo pep8

```bash
$ cd /path/to/env/app_backend/app
$ ../bin/flake8 app_backend/*
```

* Formatar o codigo pelo padrão do pep8 (black)

`$ ./bin/black ../bin/black --exclude='/migrations/' app_backend/`

## Executar o Coverage report

Após executar todos os testes unitários execute o comando abaixo

```bash
$ cd /path/to/env/app_backend/app
$ ../bin/coverage html
```

O comando gerará uma pasta chamada `htmlcov` e ao abri-lá irá localizar e abrir o arquivo `index.html` com seu navegador para ver o relatório


## Analise pelo Coverage

|Module|statements|missing|excluded|coverage|
|--- |--- |--- |--- |--- |
|Total|188|63|0|66%|
|Total|188|63|0|66%|

