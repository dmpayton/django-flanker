django-flanker
==============

[![Build Status](https://secure.travis-ci.org/dmpayton/django-flanker.png)](http://travis-ci.org/dmpayton/django-flanker)
[![Coverage Status](https://coveralls.io/repos/dmpayton/django-flanker/badge.png)](https://coveralls.io/r/dmpayton/django-flanker)
[![Downloads](https://pypip.in/d/django-flanker/badge.png)](https://pypi.python.org/pypi/django-flanker/)
[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/dmpayton/django-flanker/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

Django-flanker provides a drop-in replacement EmailFields for Django forms and
models that uses Mailgun's [flanker](https://github.com/mailgun/flanker)
library for more extensive validation.

* **Author**: [Derek Payton](http://dmpayton.com)
* **Version**: 0.2.0
* **License**: MIT

Install
-------

```
pip install django-flanker
```

Module Overview
---------------

**django_flanker.driver.DjangoCache**

A driver for Flanker's MX record cache that uses Django's built-in caching
mechanism. This driver is installed by default, but can be disabled by setting
``FLANKER_DRIVER_ENABLED`` to ``False`` in your Django site settings.

**django_flanker.forms.EmailField**

A drop-in replacement for ``django.forms.EmailField``.

**django_flanker.models.EmailField**

A drop-in replacement for ``django.db.models.EmailField``.

**django_flanker.validators.FlankerValidator**

A Django [validator](https://docs.djangoproject.com/en/dev/ref/validators/)
that uses Flanker to validate an email address. If the email address is not
valid, it tries to find a suggestion and adds it to the error message.

Usage
-----

### settings.py

```
...
INSTALLED_APPS = [
    ...
    'django_flanker',
]
```

### models.py

```
from django.db import models
from django_flanker.models import EmailField


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = EmailField()

    def __unicode__(self):
        return '{0} <{1}>'.format(self.name, self.email)
```

### forms.py

```
from django import forms
from django_flanker.forms import EmailField
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'email')
        model = Person


class EmailForm(forms.Form):
    email = EmailField()
```

Settings
--------

**FLANKER_DRIVER_ENABLED** *Default: True*

Set this to ``False`` to disable the DjangoCache Flanker driver.

**FLANKER_DRIVER_PARAMS** *Default: {}*

Custom parameters passed to the DjangoDriver. The available options are:

* **backend**: "default"
* **prefix**: "mxr:"
* **ttl**: 604800

Testing
-------

```
$ pip install -r requirements.txt
$ py.test tests/ --cov django_flanker --cov-report term-missing --pep8 django_flanker
```

...or let [Tox](https://pypi.python.org/pypi/tox) do the heavy lifting.


Changelog
---------

### v0.2.0 | 2014-01-25

* DjangoCache driver for Flanker's MX record cache.

### v0.1.0 | 2014-01-25

* Initial release
* Drop-in replacements for models.EmailField and forms.EmailField.
