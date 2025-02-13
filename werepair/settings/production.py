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

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_in_env'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Copy media files to staticfiles during collectstatic
import shutil
media_static_dir = os.path.join(STATIC_ROOT, 'media')
if os.path.exists(MEDIA_ROOT):
    if not os.path.exists(media_static_dir):
        os.makedirs(media_static_dir)
    for item in os.listdir(MEDIA_ROOT):
        source = os.path.join(MEDIA_ROOT, item)
        dest = os.path.join(media_static_dir, item)
        if os.path.isdir(source):
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(source, dest)
        else:
            shutil.copy2(source, dest)

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_NAME = 'WeRepair'

# Session settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_SECURE = True  # Use this in production

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
