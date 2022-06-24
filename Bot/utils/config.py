from random import choice

from .secrets import BASE_DIR, Secrets


SECRETS = Secrets()
MODE = SECRETS.mode

BOT_TOKEN = SECRETS.BOT_TOKEN
BOT_SECRET = SECRETS.BOT_SECRET
HEADERS = {'Authorization': BOT_SECRET}

INTERNAL_HOST = 'http://' + SECRETS.INTERNAL_HOST

if MODE == 'DEV':
    EXTERNAL_HOST = 'http://' + SECRETS.EXTERNAL_HOST
else:
    EXTERNAL_HOST = 'https://' + SECRETS.EXTERNAL_HOST


def get_photo():
    return choice(SECRETS.PHOTOS)
