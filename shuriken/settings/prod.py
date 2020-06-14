# Shuriken product environment settings

import os
gettext = lambda s: s

SECRET_KEY = 'qB-2Ta6=%RaX%)WeD4r!t%!q-imNW091QQ)7=WoP)!)--bGH=5'
DEBUG = False
ALLOWED_HOSTS = []

# ./shuriken
# Path to the level with apps/ dir and settings/ dir
PROJECT_APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# ./
# Path to the level with manage.py
PROJECT_ROOT = os.path.abspath(os.path.dirname(PROJECT_APP_ROOT))

# Utility paths
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'files')
STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, "static"),]
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
            ],
        },
    },
]

# Languages
LANGUAGES = [
    ('ja', 'Japanese'),
    ('en', 'English'),
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
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Japan'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Email
X_FRAME_OPTIONS = 'SAMEORIGIN'
EMAIL_HOST = os.environ['SHURIKEN_EMAIL_HOST']
EMAIL_PORT = os.environ['SHURIKEN_EMAIL_PORT']
EMAIL_HOST_USER = os.environ['SHURIKEN_EMAIL_ADDRESS']
EMAIL_HOST_PASSWORD = os.environ['SHURIKEN_EMAIL_PASSWORD']
EMAIL_USE_TLS = True