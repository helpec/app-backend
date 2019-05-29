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

## Build documentação API
* Exportar JSON do Postman

    Exporte sua coleção do Postman (somente suporte para Collection v2 por enquanto).
    Você poderia obter um arquivo JSON.

    Primeiro Passo: Selecione a coleção que você deseja exportar.
    ![Primeiro Passo: Selecione a coleção que você deseja exportar.](https://raw.githubusercontent.com/TitorX/Postdown/master/imgs/step-1.png)
    Segundo Passo: Encontre o botão de importação e clique nele.
    ![Segundo Passo: Encontre o botão de importação e clique nele.](https://raw.githubusercontent.com/TitorX/Postdown/master/imgs/step-2.png)
    Terceiro Passo: Exporte sua coleção como *coleção v2*.
    ![Terceiro Passo: Exporte sua coleção como *coleção v2*.](https://raw.githubusercontent.com/TitorX/Postdown/master/imgs/step-3.png)

* Rode `postdown` para gerar `markdown`da documentação
    ```bash
    $ postdown xxx.json xxx.md
    ```
