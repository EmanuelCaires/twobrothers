from .base import *

# Logging configuration
import os
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django_debug.log'),
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


DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['https://werepair-io.onrender.com/']



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



STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY', default='')
