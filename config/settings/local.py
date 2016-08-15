'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
'''

import warnings
import sys
import logging

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
SECRET_KEY = env("DJANGO_SECRET_KEY",
                 default='t69v7lq5ayk^k_)uyvjvpo(sljrcnbh)&$(rsqqjg-87160@^%')

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

# Testing
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', 'test_without_migrations')

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


# http://stackoverflow.com/a/28560805/313548
class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"


TESTS_IN_PROGRESS = False
if 'test' in sys.argv[1:] or 'jenkins' in sys.argv[1:]:
    logging.disable(logging.CRITICAL)
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )
    DEBUG = False
    TEMPLATE_DEBUG = False
    TESTS_IN_PROGRESS = True
    MIGRATION_MODULES = DisableMigrations()

MANIFEST_URL = env('MANIFEST_URL', default=None)
CORS_ORIGIN_ALLOW_ALL = True

DJOSER = {
    'SITE_NAME': 'CCDB (test)',
    'DOMAIN': 'localhost:4200',
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset?uid={uid}&token={token}',
}
