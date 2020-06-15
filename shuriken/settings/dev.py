# Development environment settings

from shuriken.settings.prod import *

DEBUG=True

ALLOWED_HOSTS = []

# Development environment uses different database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'exclusions/db.sqlite3'),
    }
}