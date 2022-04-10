from json import loads
from pathlib import Path
from base64 import b64encode


MODE = 'DEV'
BASE_DIR = Path(__file__).resolve().parent.parent


with open(BASE_DIR / 'secrets.json', 'r') as f:
    SECRETS = loads(f.read())
    SECRET_KEY = SECRETS['SECRET_KEY']

    BOT_TOKEN = SECRETS['BOT']['TOKEN']
    BOT_SECRET = SECRETS['BOT']['SECRET']
    BOT_USERNAME = SECRETS['BOT']['USERNAME']

    CLIENT_ID = SECRETS['TWITTER']['CLIENT_ID']
    CLIENT_SECRET = SECRETS['TWITTER']['CLIENT_SECRET']
    TWITTER_BEARER = SECRETS['TWITTER']['BEARER_TOKEN']
    TWITTER_AUTH = b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode()

    WEBHOOKS = SECRETS['WEBHOOKS']


DEBUG = True

ALLOWED_HOSTS = ['*']

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

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


MEDIA_URL = '/m/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
