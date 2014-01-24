from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import string_concat, ugettext_lazy as _
from flanker.addresslib import address, validate


class FlankerValidator(EmailValidator):
    suggest_fragment = _('(Did you mean: "%(suggestion)s"?)')

    def __init__(self, suggest_fragment=None, **kwargs):
        super(FlankerValidator, self).__init__(**kwargs)
        if suggest_fragment is not None:
            self.suggest_fragment = suggest_fragment

    def __call__(self, value):
        super(FlankerValidator, self).__call__(value)

        if address.validate_address(value) is None:
            suggestion = validate.suggest_alternate(value)
            if suggestion:
                message = string_concat(self.message, ' ', self.suggest_fragment)
                raise ValidationError(message, code=self.code, params={
                    'suggestion': suggestion
                })
            raise ValidationError(self.message, code=self.code)


flanker_validator = FlankerValidator()
