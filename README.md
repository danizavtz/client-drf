[![Django Logo](https://realpython.com/learn/start-django/img/django-logo-positive.png)](https://www.djangoproject.com/)
## client-drf
Cliente Django Rest Api, este projeto possui um par equivalente a esse projeto escrito em node [cliente-node](https://github.com/danizavtz/cliente-node) fiz esse projeto a fim de comparar duas implementações de uma restful api escrito em django usando o rest-framework e usando express.

## Preparação do Ambiente

Supondo que já possui o mysql instalado em sua máquina.
```
bash
$ mysql -u root -p
```
Ao logar com sucesso criar um novo banco de dados
```
sql
CREATE DATABASE clientes;
```
## Configuração da aplicação
Supondo que possui o *virtualenv* e *pip* instalados
```
bash
$ git clone https://github.com/danizavtz/client-drf.git
$ cd client-drf
$ virtualenv devenv -p $(which python3) #esse comando vai criar um ambientevirtual com python3
$ source devenv/bin/activate #ativar o ambientevirtual
$ pip install -r requirements/dev.txt #instala todos os requisitos necessários para rodar o projeto
```
Segue a minha configuração do mysql
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clientes',
        'USER': 'root',
        'PASSWORD':'admin',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```
Checar essas configurações, altere o arquivo:
client.settings.py
procure por DATABASES e faça essa configuração corresponder a sua.
Ou adapte esse arquivo para corresponder as suas configurações

Caso essas configuraçes estejam feitas com sucesso deverá ser possível executar os seguintes comandos:
```
bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Após esses passos ao acessar o endereço localhost:8000/clientes/
deverá retornar um []

## Postman
Os arquivos do postman estão na pasta postman, carregar eles no postman e fazer as requisições para verificar o funcionamento da api.

## Docker & docker-compose
Existe uma configuração para uso com docker e docker-compose
para isso basta mudar para a branch --> docker
```
Bash
$ git checkout docker
```
Desativar todas as instâncias mysql
```
Bash
$ sudo service mysql stop #para todas as instâncias
$ sudo service mysql status # certifica-se que ela não está em execução
```
Agora é só ativar as imagens
```
Bash
$ docker-compose build
$ docker-compose up
```
Para finalizar a execução do docker basta sair com ctrl+c
Para manter o serviço em segundo plano basta rodar  docker-compose up -d
