from os import environ
from typing import Literal
from pathlib import Path
from json import load
from base64 import b64encode


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def get_mode() -> str:
    NIGHTCURLY_MODE = environ.get('NIGHTCURLY_MODE')

    if NIGHTCURLY_MODE in ['DEV', 'dev']:
        return 'DEV'

    return 'BUILD'


class Secrets:
    mode: Literal['DEV', 'BUILD']

    SECRET_KEY: str

    CLIENT_ID: str
    CLIENT_SECRET: str
    TWITTER_BEARER: str
    TWITTER_AUTH: str

    WEBHOOKS: dict

    INTERNAL_HOST: str
    EXTERNAL_HOST: str
    JOIN_PHOTO: str
    INVITE_PHOTO: str

    BOT_TOKEN: str
    BOT_SECRET: str
    BOT_USERNAME: str

    def __init__(self):
        self.mode = get_mode()
        self.__set_data__()

    def __get_data__(self):
        with open(BASE_DIR / 'secrets.json', 'r') as f:
            return load(f)

    def __set_data__(self):
        data = self.__get_data__()

        self.SECRET_KEY = data['SECRET_KEY']

        self.CLIENT_ID = data['TWITTER']['CLIENT_ID']
        self.CLIENT_SECRET = data['TWITTER']['CLIENT_SECRET']
        self.TWITTER_BEARER = data['TWITTER']['BEARER_TOKEN']

        self.WEBHOOKS = data['WEBHOOKS']

        self.INTERNAL_HOST = data[self.mode]['INTERNAL_HOST']
        self.EXTERNAL_HOST = data[self.mode]['EXTERNAL_HOST']
        self.JOIN_PHOTO = data[self.mode]['JOIN_PHOTO']
        self.INVITE_PHOTO = data[self.mode]['INVITE_PHOTO']

        self.BOT_TOKEN = data[self.mode]['BOT']['TOKEN']
        self.BOT_SECRET = data[self.mode]['BOT']['SECRET']
        self.BOT_USERNAME = data[self.mode]['BOT']['USERNAME']

        self.__twitter_auth__()

    def __twitter_auth__(self):
        code = f'{self.CLIENT_ID}:{self.CLIENT_SECRET}'.encode()
        self.TWITTER_AUTH = b64encode(code).decode()
