from django import forms
from django_flanker.forms import EmailField
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'email')
        model = Person


class EmailForm(forms.Form):
    email = EmailField()
