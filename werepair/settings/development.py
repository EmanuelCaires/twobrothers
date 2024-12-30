from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=lambda v: [s.strip() for s in v.split(',')])


INSTALLED_APPS = [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}


STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')