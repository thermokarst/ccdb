import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('ccdb')

env = environ.Env()

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',  # Need this for djoser
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
)
LOCAL_APPS = (
    'ccdb.utils',
    'ccdb.users',
    'ccdb.projects',
    'ccdb.misc',
    'ccdb.locations',
    'ccdb.species',
    'ccdb.collections_ccdb',
    'ccdb.processing',
    'ccdb.experiments',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEBUG = env.bool("DJANGO_DEBUG", False)

FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

ADMINS = (
    ("""Matthew Ryan Dillon""", 'matthewrdillon@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': env.db("DATABASE_URL", default="postgres:///ccdbdjango"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

TIME_ZONE = 'UTC'

USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

STATIC_ROOT = str(ROOT_DIR('staticfiles'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = str(APPS_DIR('media'))

MEDIA_URL = '/media/'

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

ADMIN_URL = r'^admin/'
GRAPPELLI_ADMIN_TITLE = 'CCDB'

MANIFEST_URL = env('MANIFEST_URL', default=None)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_VERSIONING_CLASS':
        'rest_framework.versioning.NamespaceVersioning',
    'PAGE_SIZE': 100,
    'EXCEPTION_HANDLER':
        'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS':
        'rest_framework_json_api.metadata.JSONAPIMetadata',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

SITE_ID = 1

DJOSER = {
    'SITE_NAME': 'CCDB (test)',
    'DOMAIN': 'localhost:4200',
}
