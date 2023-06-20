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
poetry add django-federation-auditlog
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

OBS: If ```.save()``` be called to a model and the fields have the same value, log entries ```don't``` be generated.

## Including Fields

If ```include_fields``` is specified, only the fields with the given names will be included in the generated log entries.

For example, to include only the field ```name``` from class MyModel, use:

```python
from django.db import models

from django_federation_auditlog.registry import auditlog

class MyModel(models.Model):
    name = models.CharField()
    description = models.CharField()
    # Model definition goes here

auditlog.register(MyModel, include_fields=["name"])
```

## Excluding fields

Fields that are excluded will not trigger saving a new log entry and will not show up in the recorded changes.

If ```exclude_fields``` is specified the fields with the given names will not be included in the generated log entries.

For example, to exclude the field ```description```, use:

```python
from django.db import models

from django_federation_auditlog.registry import auditlog

class MyModel(models.Model):
    name = models.CharField()
    description = models.CharField()
    # Model definition goes here

auditlog.register(MyModel, exclude_fields=["description"])
```