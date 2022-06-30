#!/usr/bin/env python
"""
beta settings file for aajrewards

activate this by setting the environmental variable ENV=beta

WARNING: DON'T USE THIS IN A PRODUCTION ENVIRONMENT
"""
from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DB_NAME_DEV'),
        'USER': getenv('DB_USER_DEV'),
        'PASSWORD': getenv('DB_PASSWORD_DEV'),
        'HOST': getenv('DB_HOST_DEV'),
        'PORT': getenv('DB_PORT'),
    }
}
