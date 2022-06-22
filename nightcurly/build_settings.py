from .settings import *


MODE = 'BUILD'
DEBUG = False

ALLOWED_HOSTS = SECRETS.data[SECRETS.mode]['ALLOWED_HOSTS']

del STATICFILES_DIRS


BASE_DB = {
    'ENGINE': 'django.db.backends.mysql',
    'PORT': 3306,
    'USER': SECRETS.DB_USER,
    'PASSWORD': SECRETS.DB_PASS,
}

DATABASES = {
    'default': {
        'NAME': 'nightcurly_default',
        **BASE_DB
    },
}

STATIC_ROOT = BASE_DIR / 'static'
