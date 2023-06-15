# Django Auditlog
This project is totally based in [Django Auditlog](https://github.com/jazzband/django-auditlog/tree/master) library.

# Instalation

with pip

```shell
pip install django-federation-auditlog
```

with pipenv

```shell
pipenv install django-federation-auditlog
```

with poetry

```shell
poetry django-federation-auditlog
```

# Adding Django Federation Auditlog to your Django application

To use in your application, just add 'django-federation-auditlog' to your project’s INSTALLED_APPS setting and add 'AuditlogMiddleware' to your's MIDDLEWARE setting then run manage.py migrate to create/upgrade the necessary database structure.

```python

INSTALLED_APPS = [
    # other apps
    "django_federation_auditlog",
]
```

and 

```python

MIDDLEWARE = [
    # others middlewares
    "django_federation_auditlog.middleware.AuditlogMiddleware",
]
```

Then run

```
python manage.py migrate
```

# Usage

Auditlog can automatically log changes to objects for you. This functionality is based on Django’s signals, but linking your models to Django Federation Auditlog is even easier using signals.

```python
from django.db import models

from django_federation_auditlog.registry import auditlog

class MyModel(models.Model):
    pass
    # Model definition goes here

auditlog.register(MyModel)
```

It is recommended to place the register code (auditlog.register(MyModel)) at the bottom of your models.py file.