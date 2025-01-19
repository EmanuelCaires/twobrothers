from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost',
    cast=lambda v: [s.strip() for s in v.split(',')]
)


DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}


STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
STRIPE_API_VERSION = '2022-11-15'  # Current stable API version

# Email configuration for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
