from django.conf import settings
from flanker import addresslib
from . import driver


def setup_django_driver():
    if getattr(settings, 'FLANKER_DRIVER_ENABLED', True):
        params = getattr(settings, 'FLANKER_DRIVER_PARAMS', {})
        addresslib.set_mx_cache(driver.DjangoCache(**params))
