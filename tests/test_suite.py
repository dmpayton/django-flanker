import random
import string
from django import test
from django.core import exceptions
from django_flanker.forms import EmailField
from django_flanker.validators import flanker_validator
from flanker.addresslib import validate
from pytest import raises
from .forms import EmailForm, PersonForm


def generate_bad_email():
    pool = string.lowercase + string.digits
    local = ''.join([random.choice(pool) for x in xrange(15)])
    host = ''.join([random.choice(pool) for x in xrange(32)])
    return '{0}@{1}.com'.format(local, host)


class FlankerTests(test.TestCase):
    def test_validator(self):
        assert flanker_validator('derek.payton@gmail.com') is None
        with raises(exceptions.ValidationError):
            flanker_validator('derek.payton@g-mail.com')
        with raises(exceptions.ValidationError):
            flanker_validator(generate_bad_email())

    def test_model_form_field(self):
        form = PersonForm()
        assert isinstance(form.fields['email'], EmailField)

    def test_form_valid(self):
        form = EmailForm({'email': 'derek.payton@gmail.com'})
        assert form.is_valid() is True

    def test_form_invalid(self):
        form = EmailForm({'email': generate_bad_email()})
        assert form.is_valid() is False

    def test_form_invalid_suggest(self):
        bad_email = 'derek.payton@gmial.com'
        suggestion = validate.suggest_alternate(bad_email)
        form = EmailForm({'email': bad_email})
        assert form.is_valid() is False
        assert suggestion in form.errors['email'].as_text()
