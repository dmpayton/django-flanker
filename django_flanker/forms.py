from django import forms
from . import validators


class EmailField(forms.EmailField):
    default_validators = [validators.flanker_validator]
