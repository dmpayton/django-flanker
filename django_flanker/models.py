from django.conf import settings
from django.db import models
from flanker import addresslib
from . import driver, forms, validators


if getattr(settings, 'FLANKER_DRIVER_ENABLED', True):
    params = getattr(settings, 'FLANKER_DRIVER_PARAMS', {})
    addresslib.set_mx_cache(driver.DjangoCache(**params))


class EmailField(models.EmailField):
    default_validators = [validators.flanker_validator]

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.EmailField,
        }
        defaults.update(kwargs)
        return super(EmailField, self).formfield(**defaults)
