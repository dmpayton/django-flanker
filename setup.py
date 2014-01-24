#!/usr/bin/env python
"""
django-flanker
==============

|travis-ci|_

.. |travis-ci| image:: https://secure.travis-ci.org/dmpayton/django-flanker.png
.. _travis-ci: http://travis-ci.org/dmpayton/django-flanker


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
    keywords='django flanker email',
    maintainer='Derek Payton',
    maintainer_email='derek.payton@gmail.com',
    url='https://github.com/dmpayton/django-flanker',
    download_url='https://github.com/dmpayton/django-flanker/tarball/v%s' % __version__,
    license=__license__,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'django',
        'flanker'
    ],
    zip_safe=False,
    )
