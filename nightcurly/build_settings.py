from .settings import *


DEBUG = False

ALLOWED_HOSTS = ['5.9.226.21', 'nightcurly.art', '0.0.0.0']

del STATICFILES_DIRS

STATIC_ROOT = BASE_DIR / 'static'
