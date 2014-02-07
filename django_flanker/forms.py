from django import forms
from django.utils.translation import ugettext_lazy as _
from . import validators


class EmailField(forms.EmailField):
    default_error_messages = {
        'invalid': _('Enter a valid email address.'),
        'invalid_typo': _('Enter a valid email address. (Did you mean: "%(suggestion)s"?)')
    }
    default_validators = [validators.flanker_validator]
