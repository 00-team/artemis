from .secrets import Secrets, BASE_DIR


SECRETS = Secrets()
MODE = SECRETS.mode

BOT_TOKEN = SECRETS.BOT_TOKEN
BOT_SECRET = SECRETS.BOT_SECRET
HEADERS = {'Authorization': BOT_SECRET}

JOIN_PHOTO = SECRETS.JOIN_PHOTO
INVITE_PHOTO = SECRETS.INVITE_PHOTO

INTERNAL_HOST = 'http://' + SECRETS.INTERNAL_HOST

if MODE == 'DEV':
    EXTERNAL_HOST = 'http://' + SECRETS.EXTERNAL_HOST
else:
    EXTERNAL_HOST = 'https://' + SECRETS.EXTERNAL_HOST
