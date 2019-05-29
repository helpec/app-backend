# API Helpec - Manual

----------------

## AutenticationUser - Login

```
POST https://api.helpec.com.br/api/rest-auth/login/
```

EndPoint necessario para login do usuario na aplicação

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type| application/json||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |username|admin@admin.com|text||
> |password|admin|text||
> 

### Examples:

```bash
  curl --location --request POST "https://api.helpec.com.br/api/rest-auth/login/" \
  --header "Content-Type:  application/json" \
  --form "username=admin@admin.com" \
  --form "password=admin"
```
----------------

## AutenticationUser - RegistrationUser

```
POST https://api.helpec.com.br/api/rest-auth/registration/
```

EndPoind utilizado para fazer o registro num novo usuario no sistema

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/javascript||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |username|Jose|text||
> |email|jose@test.com|text||
> |password1|1234A5678|text||
> |password2|1234A5678|text||
> 

### Examples:

```bash
> curl --location --request POST "https://api.helpec.com.br/api/rest-auth/registration/" \
  --header "Content-Type: application/javascript" \
  --form "username=Jose" \
  --form "email=jose@test.com" \
  --form "password1=1234A5678" \
  --form "password2=1234A5678"
```
----------------

## AutenticationUser - RegistrationUser - VerifyEmail

```
POST https://api.helpec.com.br/api/rest-auth/registration/verify-email/
```

EndPoint utilizado para fazer o processo de verificação de email do usuario registrado no sistema, essa etapa é utilizada logo apos a etapa de registro do usuario

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/javascript||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |key|{{token}}|text||
> 

### Examples:

```bash
  curl --location --request POST "https://api.helpec.com.br/api/rest-auth/registration/verify-email/" \
  --header "Content-Type: application/javascript" \
  --form "key=XXXXXX"
```
----------------

## AutenticationUser - ResetPassword

```
POST https://api.helpec.com.br/api/rest-auth/password/reset/
```

EndPont utilizado para o inicio do processo de recuperação de senha do usuario, esse processo envia um email com um token para usuario

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/javascript||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |email|admin@admin.com|text||
> 

### Examples:

```bash
 curl --location --request POST "https://api.helpec.com.br/api/rest-auth/password/reset/" \
  --header "Content-Type: application/javascript" \
  --form "email=admin@admin.com"

```

----------------

## AutenticationUser - ResetPassword - Confirm

```
POST https://api.helpec.com.br/api/rest-auth/password/reset/confirm/
```

EndPont para recuperar a senha do usuario, esse endpont utiliza o token enviado ao usuario para no porcesso de `resetPassword`

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/javascript||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |uid|1234|text|uid are sent in email after calling /rest-auth/password/reset/|
> |token|5678|text|token are sent in email after calling /rest-auth/password/reset/|
> |new_password1|admin|text||
> |new_password2|admin|text||
> 

### Examples:

```bash
 curl --location --request POST "https://api.helpec.com.br/api/rest-auth/password/reset/confirm/" \
  --header "Content-Type: application/javascript" \
  --form "uid=1234" \
  --form "token=5678" \
  --form "new_password1=admin" \
  --form "new_password2=admin"
```
----------------

## AutenticationUser - UserDetais

```
GET https://api.helpec.com.br/api/rest-auth/user/
```

EndPont que recupera os dados do do usuario logado no sistema

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Authorization|Token {{token}}||
> |Content-Type|application/json||
> 

### Examples:

```bash
  curl --location --request GET "https://api.helpec.com.br/api/rest-auth/user/" \
  --header "Authorization: Token XXXXXX" \
  --header "Content-Type: application/json" \
  --data ""
```
----------------

## AutenticationUser - UserDetais - Update

```
PATCH https://api.helpec.com.br/api/rest-auth/user/
```

EndPont utilizado para atualizar os dados do usuario logado

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Authorization|Token {{token}}||
> |Content-Type|application/json||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |first_name|Administrador|text||
> |last_name|Super User|text||
> 

### Examples:

```bash
  curl --location --request PATCH "https://api.helpec.com.br/api/rest-auth/user/" \
  --header "Authorization: Token XXXXXX" \
  --header "Content-Type: application/json" \
  --form "first_name=Administrador" \
  --form "last_name=Super User"
```
----------------

## AutenticationUser - UserDetais - Override

```
PUT https://api.helpec.com.br/api/rest-auth/user/
```

Sobrescreve o usuario logado os dados enviados ou com seu valor padrão

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Authorization|Token {{token}}||
> |Content-Type|application/json||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |first_name|User2|text||
> |last_name|novo|text||
> |username|newuser|text||
> |password|1234a5678|text||
> 

### Examples:

```bash
 curl --location --request PUT "https://api.helpec.com.br/api/rest-auth/user/" \
  --header "Authorization: Token XXXXXX" \
  --header "Content-Type: application/json" \
  --form "first_name=User2" \
  --form "last_name=novo" \
  --form "username=newuser" \
  --form "password=1234a5678"
```
----------------

## ContactUser - List Constacts

```
GET https://api.helpec.com.br/api/accounts/contact
```

EndPont utilizado listar os contatos do usuario logado

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Authorization|Token {{token}}||
> |Content-Type|application/x-www-form-urlencoded||
> 

### Examples:

```bash
 curl --location --request GET "https://api.helpec.com.br/api/accounts/contact" \
  --header "Authorization: Token XXXXXX" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data ""
```
----------------

## ContactUser - Create Contact

```
POST https://api.helpec.com.br/api/accounts/contact/
```

EndPont utilizado criar um novo contatos para o usuario logado

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Authorization|Token {{token}}||
> |Content-Type|application/json||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |name|Maria|text||
> |phone|11912345678|text||
> 

### Examples:

```bash
 curl --location --request POST "https://api.helpec.com.br/api/accounts/contact/" \
  --header "Authorization: Token XXXXXX" \
  --header "Content-Type: application/json" \
  --form "name=Maria" \
  --form "phone=11912345678"
```
----------------

## OccurrenceUser - List Occurrence

```
GET https://api.helpec.com.br/api/accounts/occurrence
```

EndPont utilizado listar as ocorrencias do usuario logado

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Authorization|Token {{token}}||
> |Content-Type|application/json||
> 

### Examples:

```bash
 curl --location --request POST "https://api.helpec.com.br/api/accounts/occurrence/" \
  --header "Authorization: Token XXXXXX" \
  --header "Content-Type: application/json" \
  --form "date_creation=2019-04-15 12:00:00" \
  --form "location=123456789"
```
----------------

## OccurrenceUser - Create Occurrence

```
POST https://api.helpec.com.br/api/accounts/occurrence/
```

EndPont utilizado para criar uma nova ocorrencia para o usuario logado

----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Authorization|Token {{token}}||
> |Content-Type|application/json||
> 
> **Body**
> 
> |Key|Value|Type|Description|
> |---|---|---|---|
> |date_creation|2019-04-15 12:00:00|text||
> |location|123456789|text||
> 

### Examples:

```bash
 curl --location --request POST "https://api.helpec.com.br/api/accounts/occurrence/" \
  --header "Authorization: Token XXXXXX" \
  --header "Content-Type: application/json" \
  --form "date_creation=2019-04-15 12:00:00" \
  --form "location=123456789"
```