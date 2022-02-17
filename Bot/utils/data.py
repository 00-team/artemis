from typing import Literal

from json import load
from json import dump
from os.path import exists
from logging import getLogger

logger = getLogger(__name__)


def read_json(filename: str, default=None):
    if exists(filename):
        with open(filename, 'r') as f:
            return load(f)

    return default


def write_json(filename: str, json):
    with open(filename, 'w') as f:
        dump(json, f)


LANG = Literal['en', 'ru']


def update_users(user_id, lang: LANG = 'en', change: bool = True) -> bool:
    try:
        filename = './data/users.json'
        users = read_json(filename, [])

        for user in users:
            if user['id'] == user_id:
                if user['lang'] != lang and change:
                    user['lang'] = lang
                    write_json(filename, users)

                return True
        else:
            users.append({'id': user_id, 'lang': lang})
            write_json(filename, users)
            return False

    except Exception as e:
        logger.error(e)


def update_data(chats):
    try:
        filename = './data/main.json'
        data = read_json(filename)

        if not data:
            raise ValueError('data file not found')

        data['chats'] = chats

        write_json(filename, data)
    except Exception as e:
        logger.error(e)


def get_token() -> str:
    with open('../secrets.json', 'r') as f:
        return load(f)['BOT_TOKEN']