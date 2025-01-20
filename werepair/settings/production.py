from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']
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
        'HOST': 'postgresql://werepair_io_user:aFrB95herlY1tsJeIdl7McmBXoyxblwu@dpg-ctjus82j1k6c73cln0ug-a.frankfurt-postgres.render.com/werepair_io',
        'PORT': '5432',
    }

}

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY', default='')