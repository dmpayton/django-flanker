from django.db import models
from . import forms, validators


class EmailField(models.EmailField):
    default_validators = [validators.flanker_validator]

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.EmailField,
        }
        defaults.update(kwargs)
        return super(EmailField, self).formfield(**defaults)
