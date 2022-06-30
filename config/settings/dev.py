#!/usr/bin/env python
"""
dev settings file for aajrewards

activate this by setting the environmental variable ENV=dev

WARNING: DON'T USE THIS IN A PRODUCTION ENVIRONMENT
"""
from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DB_NAME_DEV'),
        'USER': getenv('DB_USER_DEV'),
        'PASSWORD': getenv('DB_PASSWORD_DEV'),
        'HOST': getenv('DB_HOST_DEV'),
        'PORT': getenv('DB_PORT'),
    },
}
