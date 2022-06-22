from base64 import b64encode
from json import load
from os import environ
from pathlib import Path
from typing import Literal


BASE_DIR = Path(__file__).resolve().parent.parent


def get_mode() -> str:
    NIGHTCURLY_MODE = environ.get('NIGHTCURLY_MODE')

    if NIGHTCURLY_MODE in ['DEV', 'dev']:
        return 'DEV'

    return 'BUILD'


def get_settings() -> str:
    if get_mode() == 'DEV':
        return 'nightcurly.settings'

    return 'nightcurly.build_settings'


class Secrets:
    mode: Literal['DEV', 'BUILD']

    SECRET_KEY: str
    SECRET_TOKEN_FILE: str

    CLIENT_ID: str
    CLIENT_SECRET: str
    TWITTER_BEARER: str
    TWITTER_AUTH: str

    WEBHOOKS: dict

    INTERNAL_HOST: str
    EXTERNAL_HOST: str

    BOT_TOKEN: str
    BOT_SECRET: str
    BOT_USERNAME: str

    DB_USER: str
    DB_PASS: str

    data: dict

    def __init__(self):
        self.mode = get_mode()
        self.__set_data__()

    def __get_data__(self):
        with open(BASE_DIR / 'secrets.json', 'r') as f:
            return load(f)

    def __set_data__(self):
        data = self.__get_data__()
        self.data = data

        self.SECRET_KEY = data['SECRET_KEY']
        self.SECRET_TOKEN_FILE = data['SECRET_TOKEN_FILE']

        self.CLIENT_ID = data['TWITTER']['CLIENT_ID']
        self.CLIENT_SECRET = data['TWITTER']['CLIENT_SECRET']
        self.TWITTER_BEARER = data['TWITTER']['BEARER_TOKEN']

        self.WEBHOOKS = data['WEBHOOKS']

        self.INTERNAL_HOST = data[self.mode]['INTERNAL_HOST']
        self.EXTERNAL_HOST = data[self.mode]['EXTERNAL_HOST']

        self.BOT_TOKEN = data[self.mode]['BOT']['TOKEN']
        self.BOT_SECRET = data[self.mode]['BOT']['SECRET']
        self.BOT_USERNAME = data[self.mode]['BOT']['USERNAME']

        self.DB_USER = data[self.mode]['DATABASE']['USER']
        self.DB_PASS = data[self.mode]['DATABASE']['PASSWORD']

        self.__twitter_auth__()

    def __twitter_auth__(self):
        code = f'{self.CLIENT_ID}:{self.CLIENT_SECRET}'.encode()
        self.TWITTER_AUTH = b64encode(code).decode()
