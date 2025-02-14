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

# Middleware Configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise must be above all other middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  
]

# Static Configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_in_env'),
]

# Media Configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Storage Configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
DEFAULT_FILE_STORAGE = 'core.storage.MediaStorage'

# WhiteNoise Configuration
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
WHITENOISE_MANIFEST_STRICT = False

# Ensure media files are copied to static directory during deployment
import os
import shutil

# Create media directory in static if it doesn't exist
media_static = os.path.join(STATIC_ROOT, 'media')
if not os.path.exists(media_static):
    os.makedirs(media_static)

# Copy existing media files to static directory
if os.path.exists(MEDIA_ROOT):
    for root, dirs, files in os.walk(MEDIA_ROOT):
        for file in files:
            src = os.path.join(root, file)
            rel_path = os.path.relpath(src, MEDIA_ROOT)
            dst = os.path.join(media_static, rel_path)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_NAME = 'WeRepair'

# Session settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_SECURE = True

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
        'HOST': 'dpg-ctjus82j1k6c73cln0ug-a.frankfurt-postgres.render.com',
        'PORT': '5432',
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')
