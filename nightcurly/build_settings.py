from .settings import *

MODE = 'BUILD'
DEBUG = False

ALLOWED_HOSTS = SECRETS.data[SECRETS.mode]['ALLOWED_HOSTS']

del STATICFILES_DIRS

STATIC_ROOT = BASE_DIR / 'static'
