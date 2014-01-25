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
* **Version**: 0.1.0
* **License**: MIT

Install
-------

```
pip install django-flanker
```

Usage
-----

### models.py

Replace ``django.db.models.EmailField`` with ``django_flanker.models.EmailFild``:

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

Replace ``django.forms.EmailField`` with ``django_flanker.forms.EmailFild``:

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

Testing
-------

```
$ pip install -r requirements.txt
$ py.test tests/ --cov django_flanker
```

...or let [Tox](https://pypi.python.org/pypi/tox) do the heavy lifting.
