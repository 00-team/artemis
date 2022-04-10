from os import environ
from json import load
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

if environ.get('NIGHTCURLY_MODE') == 'DEV':
    MODE = 'DEV'
else:
    MODE = 'BUILD'


with open(BASE_DIR / 'secrets.json', 'r') as f:
    SECRETS = load(f)

    BOT_TOKEN = SECRETS['BOT']['TOKEN']
    BOT_SECRET = SECRETS['BOT']['SECRET']
    HEADERS = {'Authorization': BOT_SECRET}

    INTERNAL_HOST = 'http://' + SECRETS[MODE]['INTERNAL_HOST']
    EXTERNAL_HOST = 'http://' + SECRETS[MODE]['EXTERNAL_HOST']
