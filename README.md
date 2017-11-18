[![Django Logo](https://realpython.com/learn/start-django/img/django-logo-positive.png)](https://www.djangoproject.com/)
## client-drf
Client Django Rest Api

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
##Configuração da aplicação
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