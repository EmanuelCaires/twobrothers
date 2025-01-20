from .base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost',
    cast=lambda v: [host.strip() for host in v.split(',')]
)

# PostgreSQL Database Configuration
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL', default='postgresql://werepair_io_user:aFrB95herlY1tsJeIdl7McmBXoyxblwu@dpg-ctjus82j1k6c73cln0ug-a.frankfurt-postgres.render.com/werepair_io'))
}

# Stripe Configuration
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='your_test_public_key')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='your_test_secret_key')
STRIPE_API_VERSION = '2022-11-15'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static and Media Files Configuration
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [BASE_DIR / 'static_in_env']
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media_root'
