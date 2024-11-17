from .base import *

DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

# CSRF Trusted Origins for production
CSRF_TRUSTED_ORIGINS = [
    'https://8000-emanuelcaire-werepairio-pwt2icriu17.ws-eu116.gitpod.io',
    'http://8000-emanuelcaire-werepairio-pwt2icriu17.ws-eu116.gitpod.io',
]

# CSRF and Session Cookie Settings
CSRF_COOKIE_SECURE = True  # Ensure the CSRF cookie is sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensure session cookies are sent over HTTPS

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Database configuration for production (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),  # Use environment variable for the port if needed
    }
}

# Stripe keys for live environment
STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')

