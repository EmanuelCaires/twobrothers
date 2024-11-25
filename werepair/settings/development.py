from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    '8000-emanuelcaire-werepairio-rpnsaofi34a.ws-eu116.gitpod.io',
    'localhost',
    '127.0.0.1',
]

CSRF_TRUSTED_ORIGINS = [
    'https://8000-emanuelcaire-werepairio-rpnsaofi34a.ws-eu116.gitpod.io',
]

# Email backend (console for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}

# Database configuration for development (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe test keys (from .env or environment variables)
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default=None)
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default=None)

