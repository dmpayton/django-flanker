#!/usr/bin/env python
"""
django-flanker
==============

|travis-ci|_ |coveralls|_ |downloads|_

Django-flanker provides a drop-in replacement EmailFields for Django forms and
models that uses Mailgun's `flanker <https://github.com/mailgun/flanker>`_
library for more extensive validation.

.. |travis-ci| image:: https://secure.travis-ci.org/dmpayton/django-flanker.png
.. _travis-ci: http://travis-ci.org/dmpayton/django-flanker

.. |coveralls| image:: https://coveralls.io/repos/dmpayton/django-flanker/badge.png
.. _coveralls: https://coveralls.io/r/dmpayton/django-flanker

.. |downloads| image:: https://pypip.in/d/django-flanker/badge.png
.. _downloads: https://pypi.python.org/pypi/django-flanker/

"""

from django_flanker import __version__, __description__, __license__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='django-flanker',
    version=__version__,
    description=__description__,
    long_description=__doc__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    keywords='django flanker mailgun email validation',
    maintainer='Derek Payton',
    maintainer_email='derek.payton@gmail.com',
    url='https://github.com/dmpayton/django-flanker',
    download_url='https://github.com/dmpayton/django-flanker/tarball/v%s' % __version__,
    license=__license__,
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django',
        'flanker'
    ],
    zip_safe=False,
    )
