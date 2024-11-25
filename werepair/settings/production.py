from .base import *
import os

DEBUG = config('DEBUG', cast=bool, default=False)

# Allowed Hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '8000-emanuelcaire-werepairio-pwt2icriu17.ws-eu116.gitpod.io',
]


# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://8000-emanuelcaire-werepairio-pwt2icriu17.ws-eu116.gitpod.io',
    'https://localhost',
    'https://127.0.0.1',
]



# Secure cookies based on environment
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG

# Database Configuration (PostgreSQL for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME', default='default_db_name'),
        'USER': config('DB_USER', default='default_user'),
        'PASSWORD': config('DB_PASSWORD', default='default_password'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Stripe Keys (Live for production)
STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')



