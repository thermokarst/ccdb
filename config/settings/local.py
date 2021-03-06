import warnings
import sys
import logging

from .base import *  # noqa


with warnings.catch_warnings(record=True) as warning:
    environ.Env.read_env('.env')
    for w in warning:
        print(w.message)

DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env("DJANGO_SECRET_KEY",
                 default='t69v7lq5ayk^k_)uyvjvpo(sljrcnbh)&$(rsqqjg-87160@^%')

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

INSTALLED_APPS += ('django_extensions',)

INTERNAL_IPS = ('127.0.0.1', )

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TESTS_IN_PROGRESS = False
if 'test' in sys.argv[1:] or 'jenkins' in sys.argv[1:]:
    logging.disable(logging.CRITICAL)
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )
    DEBUG = False
    TEMPLATE_DEBUG = False
    TESTS_IN_PROGRESS = True
    MIGRATION_MODULES = {app[app.rfind('.') + 1:]: None
                         for app in INSTALLED_APPS}

MANIFEST_URL = env('MANIFEST_URL', default=None)
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ('localhost:4200',)

DJOSER = {
    'SITE_NAME': 'CCDB (test)',
    'DOMAIN': 'localhost:4200',
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset?uid={uid}&token={token}',
}
