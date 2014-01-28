from django import test
from django.core import exceptions
from django.core.cache import get_cache
from django_flanker.forms import EmailField
from django_flanker.validators import flanker_validator
from flanker import addresslib
from flanker.addresslib import validate
from mock import patch
from pytest import raises
from .forms import EmailForm, PersonForm

GMAIL_MX_RECORD = 'sample.gmail-smtp-in.l.google.com'


def mock_exchanger_lookup(arg, metrics=False):
    ''' A mock exchanger lookup that is valid only for gmail.com. '''
    mtimes = {'mx_lookup': 0, 'dns_lookup': 0, 'mx_conn': 0}
    mx_record = None
    if arg == 'gmail.com':
        mx_record = GMAIL_MX_RECORD
    return (mx_record, mtimes)


@patch.object(validate, 'mail_exchanger_lookup', mock_exchanger_lookup)
class FlankerTests(test.TestCase):
    def test_validator(self):
        assert flanker_validator('derek.payton@gmail.com') is None
        with raises(exceptions.ValidationError):
            flanker_validator('user@bad-email.com')

    def test_model_form_field(self):
        form = PersonForm()
        assert isinstance(form.fields['email'], EmailField)

    def test_form_valid(self):
        form = EmailForm({'email': 'derek.payton@gmail.com'})
        assert form.is_valid() is True

    def test_form_invalid(self):
        form = EmailForm({'email': 'user@bad-email.com'})
        assert form.is_valid() is False

    def test_form_invalid_suggest(self):
        bad_email = 'derek.payton@gmial.com'
        suggestion = validate.suggest_alternate(bad_email)
        form = EmailForm({'email': bad_email})
        assert form.is_valid() is False
        assert suggestion in form.errors['email'].as_text()

    def test_driver_keytransform(self):
        assert addresslib.mx_cache.__keytransform__('gmail.com') == 'mxr:gmail.com'

    def test_driver_set(self):
        cache = get_cache('default')
        addresslib.mx_cache['gmail.com'] = GMAIL_MX_RECORD
        assert cache.get('mxr:gmail.com') == GMAIL_MX_RECORD

    def test_driver_get(self):
        addresslib.mx_cache['gmail.com'] = GMAIL_MX_RECORD
        assert addresslib.mx_cache['gmail.com'] == GMAIL_MX_RECORD

    def test_driver_delete(self):
        cache = get_cache('default')
        addresslib.mx_cache['gmail.com'] = GMAIL_MX_RECORD
        del addresslib.mx_cache['gmail.com']
        assert cache.get('gmail.com') is None
