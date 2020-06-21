# Shuriken product environment settings

import os
from distutils.util import strtobool
gettext = lambda s: s

DEBUG = False

try:
    SHURIKEN_ENVVAR_TEST= os.environ['SHURIKEN_KEY_TEST']
except KeyError:
    SHURIKEN_ENVVAR_TEST = 'This test variable was not set and Shuriken autoloaded it.'

try:
    SHURIKEN_DEV_FEATURES = strtobool(os.environ['SHURIKEN_DEV_FEATURES'])
except KeyError:
    SHURIKEN_DEV_FEATURES = False

try:
    SHURIKEN_MULTILANGUAGE = strtobool(os.environ['SHURIKEN_MULTILANGUAGE'])
except KeyError:
    SHURIKEN_MULTILANGUAGE = False

try:
    SECRET_KEY = os.environ['SHURIKEN_SECRET_KEY']
except KeyError:
    SECRET_KEY = 'aBx52Xa-7ZhqQ69Z1YsT2462--41%z(00tRa6Xb7-2$R--)1bHXQe'

try:
    EMAIL_HOST = os.environ['SHURIKEN_EMAIL_HOST']
except KeyError:
    EMAIL_HOST = 'Environment variable could not be found (EMAIL_HOST)'

try:
    EMAIL_PORT = os.environ['SHURIKEN_EMAIL_PORT']
except KeyError:
    EMAIL_PORT = 'Environment variable could not be found (EMAIL_PORT)'

try:
    EMAIL_HOST_USER = os.environ['SHURIKEN_EMAIL_ADDRESS']
except KeyError:
    EMAIL_HOST_USER = 'Environment variable could not be found (EMAIL_ADDRESS)'

try:
    EMAIL_HOST_PASSWORD = os.environ['SHURIKEN_EMAIL_PASSWORD']
except KeyError:
    EMAIL_HOST_PASSWORD = 'Environment variable could not be found'

try:
    SHURIKEN_DB_ENGINE = os.environ['SHURIKEN_DB_ENGINE']
except KeyError:
    SHURIKEN_DB_ENGINE = 'django.db.backends.postgresql_psycopg2'

try:
    SHURIKEN_DB_NAME = os.environ['SHURIKEN_DB_NAME']
except KeyError:
    SHURIKEN_DB_NAME = 'Environment variable could not be found (DB_NAME)'

try:
    SHURIKEN_DB_USER = os.environ['SHURIKEN_DB_USER']
except KeyError:
    SHURIKEN_DB_USER = 'Environment variable could not be found (DB_USER)'

try:
    SHURIKEN_DB_PASSWORD = os.environ['SHURIKEN_DB_PASSWORD']
except KeyError:
    SHURIKEN_DB_PASSWORD = 'Environment variable could not be found (DB_PASSWORD)'

try:
    SHURIKEN_DB_HOST = os.environ['SHURIKEN_DB_HOST']
except KeyError:
    SHURIKEN_DB_HOST = 'Environment variable could not be found (DB_HOST)'

try:
    SHURIKEN_DB_PORT = os.environ['SHURIKEN_DB_PORT']
except KeyError:
    SHURIKEN_DB_PORT = 'Environment variable could not be found (DB_PORT)'


SHURIKEN_VERSION = '0.1'

# Security
ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Databases
CONN_MAX_AGE = None # enable persistent connections; default 0 (terminate at max-life)

# ./shuriken
# Path to the level with apps/ dir and settings/ dir
PROJECT_APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# ./
# Path to the level with manage.py
PROJECT_ROOT = os.path.abspath(os.path.dirname(PROJECT_APP_ROOT))

# Utility paths
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'files')
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static"),)
LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'locale'),)

# Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'common',
    'shuriken.apps.core',
    'shuriken.apps.blog',
    'shuriken.apps.reader',
    'shuriken.apps.resources',
    'shuriken.apps.spider',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Options
OPTIONS={
    'libraries': {
        'setvar': 'common.templatetags.setvar',
    },
}

# Urls
ROOT_URLCONF = 'shuriken.urls'
STATIC_URL = '/static/'
MEDIA_URL = '/files/'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_ROOT],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shuriken.apps.core.context_processors.core'
            ],
        },
    },
]



# WSGI
WSGI_APPLICATION = 'shuriken.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# Languages
if SHURIKEN_MULTILANGUAGE:
    LANGUAGE_CODE = 'en'    
    LANGUAGES = [
        ('ja', gettext('Japanese')),
        ('en', gettext('English')),
    ]

else:
    LANGUAGE_CODE = 'en'
    LANGUAGES = [
        ('en', gettext('English')),
    ]
    
TIME_ZONE = 'Japan'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Email
X_FRAME_OPTIONS = 'DENY' # Sameorigin
EMAIL_USE_TLS = True

# Databases
DATABASES = {
    'default': {
        'ENGINE': SHURIKEN_DB_ENGINE,
        'NAME': SHURIKEN_DB_NAME,
        'USER': SHURIKEN_DB_USER,
        'PASSWORD': SHURIKEN_DB_PASSWORD,
        'HOST': SHURIKEN_DB_HOST,
        'PORT': SHURIKEN_DB_PORT,
    }
}