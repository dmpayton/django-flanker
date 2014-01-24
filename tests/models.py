from django.db import models
from django_flanker.models import EmailField


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = EmailField(max_length=254)

    def __unicode__(self):
        return '{0} <{1}>'.format(self.name, self.email)
