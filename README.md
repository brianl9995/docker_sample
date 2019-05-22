# Docker

Proyecto docker Web de ejemplo para ejecutar: 
  - Django 2.2 (Con django-celery-results)
  - Celery 4.3
  - PostgreSQL 11.3
  - RabbitMQ 3


### Prerequisites

Se debe tener instalado docker y docker-compose https://docs.docker.com/compose/


### Installing

Ejecutar en la raiz del proyecto:

```
sudo docker-compose up
```

Una vez ejecutando, se procede a ejecutar las migraciones y crear un super usuario

```
$ sudo docker-compose exec web bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

Luego, entrar a http://localhost:8000/ ingresar un mensaje y revisar en el admin el resultado http://localhost:8000/admin/django_celery_results/taskresult/
