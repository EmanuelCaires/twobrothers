from .base import *

DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = [
    'ip-address',  # Replace with your production IP or domain
    'www.your-website.com',  # Replace with your domain
]

CSRF_TRUSTED_ORIGINS = [
    'https://www.your-website.com',  # Replace with your domain
]

# Email backend (SMTP for production)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')  # E.g., smtp.gmail.com for Gmail
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Your email account user
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Your email account password
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='webmaster@yourdomain.com')

# Database (PostgreSQL for production)
# werepair.io/settings/production.py or your main settings file

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'werepair_io',
        'USER': 'werepair_io_user',
        'PASSWORD': 'aFrB95herlY1tsJeIdl7McmBXoyxblwu',
        'HOST': 'postgresql://werepair_io_user:aFrB95herlY1tsJeIdl7McmBXoyxblwu@dpg-ctjus82j1k6c73cln0ug-a.frankfurt-postgres.render.com/werepair_io',
        'PORT': '5432',
    }
}




# Stripe (live keys)
STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')  # Live public key
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')  # Live secret key

# Security settings for production
SECURE_SSL_REDIRECT = True  # Forces redirect to HTTPS
SESSION_COOKIE_SECURE = True  # Ensures cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookies are only sent over HTTPS
X_FRAME_OPTIONS = 'DENY'  # Protects against clickjacking

# Additional security settings
SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for a year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

