from .base import *

# Logging configuration
import os
import logging

# Ensure the logs directory exists
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'django_debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

DEBUG = False
ALLOWED_HOSTS = ['werepair-io.onrender.com', '127.0.0.1']

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_NAME = 'WeRepair'

# Admin configuration
ADMINS = [('Emanuel Caires', 'emanuelcaires1@gmail.com')]


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'werepair_io',
        'USER': 'werepair_io_user',
        'PASSWORD': 'aFrB95herlY1tsJeIdl7McmBXoyxblwu',
        'HOST': 'dpg-ctjus82j1k6c73cln0ug-a.frankfurt-postgres.render.com',  # Just the host here
        'PORT': '5432',  # Default port
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')
