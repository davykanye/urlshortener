#!/usr/bin/env python
"""
production settings file for aajrewards

activate this by setting the environmental variable ENV=prod
"""
from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DB_NAME'),
        'USER': getenv('DB_USER'),
        'PASSWORD': getenv('DB_PASSWORD'),
        'HOST': getenv('DB_HOST'),
        'PORT': getenv('DB_PORT'),
    }
}


# CORS SETTINGS
CORS_ALLOW_ALL_ORIGINS: False