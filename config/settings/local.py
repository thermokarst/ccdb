'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
'''

import warnings

from .base import *  # noqa


with warnings.catch_warnings(record=True) as warning:
    environ.Env.read_env('.env')
    for w in warning:
        print(w.message)


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='t69v7lq5ayk^k_)uyvjvpo(sljrcnbh)&$(rsqqjg-87160@^%')

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')


# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ('127.0.0.1', )

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


DJOSER = {
    'SITE_NAME': 'CCDB (test)',
    'DOMAIN': 'localhost:4200',
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset?uid={uid}&token={token}',
}
