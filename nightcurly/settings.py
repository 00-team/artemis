from base64 import b64encode
from pathlib import Path
from json import loads

BASE_DIR = Path(__file__).resolve().parent.parent
BOT_USERNAME = 'nightcurlybot'

with open(BASE_DIR / 'secrets.json', 'r') as f:
    secrets = loads(f.read())
    SECRET_KEY = secrets['SECRET_KEY']
    BOT_TOKEN = secrets['BOT_TOKEN']
    BOT_SECRET = secrets['BOT_SECRET']
    CLIENT_ID = secrets['CLIENT_ID']
    CLIENT_SECRET = secrets['CLIENT_SECRET']
    TWITTER_BEARER = secrets['TWITTER_BEARER']
    WEBHOOKS = secrets['WEBHOOKS']
    TWITTER_AUTH = b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()
    del secrets

DEBUG = False

ALLOWED_HOSTS = ['5.9.226.21', 'nightcurly.art',
                 '0.0.0.0', 'localhost', '127.0.0.1']

LOGIN_URL = f'//t.me/{BOT_USERNAME}?start=login'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps
    'Collection.apps.CollectionConfig',
    'Account.apps.AccountConfig',
    'Api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nightcurly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'nightcurly/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nightcurly.wsgi.application'

DATABASES_DIR = BASE_DIR / 'databases'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASES_DIR / 'default.db',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/s/'

# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


MEDIA_URL = '/m/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
