# Python + Flask

Workshop para disciplina `MATC82 - Sistemas Web`, da UFBA, lecionada pela professora Gabriela Mota.

## O trabalho

### Requisitos

* Fazer um workshop utilizando a linguagem Python voltada para web
* Workshop prático, mas que tenha um pouco de conteúdo teórico

### Projeto

* Escolhido microframework Flask
* Aplicação de lista de afazeres
* Fazer a aplicação do zero ao entregável ao cliente

### Equipe

* [Elias Maciel](https://github.com/e321maciel)
* [Felipe Regino](https://github.com/feliperegino)
* [Gildásio Júnior](https://github.com/gjuniioor)
* [Neyde Karen](https://github.com/nykaren)
* [Rafael Coelho](https://github.com/rllcoelho)

## Etapas

### 01 - Frontend

Download dos frameworks:

* [GainTime](https://gaintime.github.io)
* [Font Awesome](http://fontawesome.io/)
* [DataTables](https://datatables.net)
* [jQuery](https://jquery.com)

#### Gaintime

Framework frontend para estilização e interação do usuário na página.

Com ele montamos o layout da aplicação, como formulários, tabela, modals, botões ...

#### Font Awesome

Framework frontend para inserção de ícones nas páginas web.

Todos ícones que tem na aplicação foi utilizando esse framework.

#### DataTables

Plugin do jQuery para realização de ordenação, paginação e buscas em tabelas.

Todas essas funcionalidades na tabela de listagem das opções são feitas com esse plugin.

#### jQuery

A princípio entrou por ser dependência do DataTables, mas posteriormente iremos utilizar mais ele.

### 02 - Ambiente - Flask

Primeiramente, vamos atualizar o sistema:

~~~
$ sudo apt update
~~~

Depois, instalar virtual enviroment do Python:

~~~
$ sudo apt install python-virtualenv -y
~~~

Criar ambiente virtual:

~~~
$ virtualenv -p `which python3` venv
$ echo venv >> .gitignore
$ source venv/bin/activate
~~~

Instalar Flask:

~~~
$ pip install Flask
~~~

* Hello world com Flask!

Gerenciamento de dependências:

~~~
$ pip freeze > requirements.txt
~~~

### 03 - Template Index

* Criar pasta templates
* Mover index.html para templates
* Mover assets para static
* Inserir na template index.html via static
* Renderizar o template

### 04 - Ambiente - Mongo

* Criar banco no MongoLabs
* Instalar `mongoengine`:

~~~
$ pip install mongoengine
$ pip freeze > requirements.txt
~~~

* Conectar!

> **Boas práticas**:
> * Env config file
> * Excluir do git
> * Ler no 


### 05 - Create

* Editar formulário
* Criar entidade Task
* Criar método create
* Aumentar .gitignore

~~~
$ echo __pycache__ >> .gitignore
~~~

### 06 - Read

* Fazer consulta dos dados
* Passar dados para o template
* Renderizar informações no front

### 07 - Delete

* Criar método para deletar
* Editar formulário

### 08 - Mark Complete

* Criar método para marcar como completo
* Editar formulário

### 09 - Edit

* Editar formulário
  * Se atentar ao método de envio
* Construir método de edição

### 10 - Heroku

* Procfile
* runtime
* Retirar pgkresources do requirements.txt

> **Bônus: ** HEROKU como Continous Integration