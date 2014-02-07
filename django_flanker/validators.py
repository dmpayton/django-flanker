from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from flanker.addresslib import address, validate


class FlankerValidator(object):
    code_invalid = 'invalid'
    code_typo = 'invalid_typo'
    message_invalid = _('Enter a valid email address.')
    message_typo = _('Enter a valid email address. (Did you mean: "%(suggestion)s"?)')

    def __init__(self, suggest_fragment=None, **kwargs):
        super(FlankerValidator, self).__init__(**kwargs)
        if suggest_fragment is not None:
            self.suggest_fragment = suggest_fragment

    def __call__(self, value):
        validate_email(value)
        value = force_text(value)

        if value and address.validate_address(value) is None:
            suggestion = validate.suggest_alternate(value)
            if suggestion:
                raise ValidationError(self.message_typo, code=self.code_typo,
                    params={'suggestion': suggestion})
            raise ValidationError(self.message_invalid, code=self.code_invalid)


flanker_validator = FlankerValidator()
