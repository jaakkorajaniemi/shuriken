# Shuriken product environment settings

import os
from distutils.util import strtobool
gettext = lambda s: s

DEBUG = False

SHURIKEN_DEV_FEATURES = strtobool(os.environ['SHURIKEN_DEV_FEATURES']) if os.environ['SHURIKEN_DEV_FEATURES'] is not None else False
SHURIKEN_MULTILANGUAGE = strtobool(os.environ['SHURIKEN_MULTILANGUAGE']) if os.environ['SHURIKEN_DEV_FEATURES'] is not None else False
SHURIKEN_VERSION = '0.1'

# Security
SECRET_KEY = os.environ['SHURIKEN_SECRET_KEY'] if os.environ['SHURIKEN_SECRET_KEY'] is not None else 'aBx52Xa-7ZhqQ69Z1YsT2462--41%z(00tRa6Xb7-2$R--)1bHXQe'
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
EMAIL_HOST = os.environ['SHURIKEN_EMAIL_HOST'] if os.environ['SHURIKEN_EMAIL_HOST'] is not None else 'error'
EMAIL_PORT = os.environ['SHURIKEN_EMAIL_PORT'] if os.environ['SHURIKEN_EMAIL_PORT'] is not None else 'error'
EMAIL_HOST_USER = os.environ['SHURIKEN_EMAIL_ADDRESS'] if os.environ['SHURIKEN_EMAIL_ADDRESS'] is not None else 'error'
EMAIL_HOST_PASSWORD = os.environ['SHURIKEN_EMAIL_PASSWORD'] if os.environ['SHURIKEN_EMAIL_PASSWORD'] is not None else 'error'
EMAIL_USE_TLS = True

# Databases
DATABASES = {
    'default': {
        'ENGINE': os.environ['SHURIKEN_DB_ENGINE'] if os.environ['SHURIKEN_DB_ENGINE'] is not None else 'error',
        'NAME': os.environ['SHURIKEN_DB_NAME'] if os.environ['SHURIKEN_DB_NAME'] is not None else 'error',
        'USER': os.environ['SHURIKEN_DB_USER'] if os.environ['SHURIKEN_DB_USER'] is not None else 'error',
        'PASSWORD': os.environ['SHURIKEN_DB_PASSWORD'] if os.environ['SHURIKEN_DB_PASSWORD'] is not None else 'error',
        'HOST': os.environ['SHURIKEN_DB_HOST'] if os.environ['SHURIKEN_DB_HOST'] is not None else 'error',
        'PORT': os.environ['SHURIKEN_DB_PORT'] if os.environ['SHURIKEN_DB_PORT'] is not None else 'error',
    }
}