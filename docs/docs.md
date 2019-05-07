# Documentação da aplicação

## Instalar construtor da documentação

```bash
$ cd /path/to/env/app_backend/app
$ ../bin/pip install mkdocs
```

## Executar `build` da documentação 

```bash
$ cd /path/to/env/app_backend/app
$ ../bin/mkdocs build
```

## Deploy documentação

* Aticionar git-remote remote  
```bash
$ cd /path/to/env/app_backend/app
$ git remote add github_io git@github.com:helpec/helpec.github.io.git
```

* Enviar arquivos `buildados`
```bash
$ cd /path/to/env/app_backend/app
$ ../bin/mkdocs gh-deploy
```
