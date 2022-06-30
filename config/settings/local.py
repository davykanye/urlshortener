#!/usr/bin/env python
"""
local settings file for aajrewards

activate this by setting the environmental variable ENV=local

WARNING: DON'T USE THIS IN A PRODUCTION OR BETA ENVIRONMENT
"""
from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('DB_NAME_LOCAL'),
        'USER': getenv('DB_USER_LOCAL'),
        'PASSWORD': getenv('DB_PASSWORD_LOCAL'),
        'HOST': getenv('DB_HOST_LOCAL'),
        'PORT': getenv('DB_PORT'),

        'TEST': {

        },
    },
}


# CORS SETTINGS

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000'
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]

CORS_ALLOW_ALL_ORIGINS: True