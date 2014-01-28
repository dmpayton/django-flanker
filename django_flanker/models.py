from django.db import models
from . import forms, utils, validators

utils.setup_django_driver()


class EmailField(models.EmailField):
    default_validators = [validators.flanker_validator]

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.EmailField,
        }
        defaults.update(kwargs)
        return super(EmailField, self).formfield(**defaults)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules(
        [], ['^django_flanker\.models\.EmailField']
    )
except ImportError:
    pass
