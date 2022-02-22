from json import load
from json import dump
from os.path import exists
from logging import getLogger

USER_DB = './data/users.db'
HOST = 'http://127.0.0.1:7000/'

logger = getLogger(__name__)


def read_json(filename: str, default=None):
    if exists(filename):
        with open(filename, 'r') as f:
            return load(f)

    return default


def write_json(filename: str, json):
    with open(filename, 'w') as f:
        dump(json, f)


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
        data = load(f)
        return (data['BOT_TOKEN'], data['BOT_SECRET'])


def get_date() -> dict:
    return read_json('./data/main.json', {})


MDC = [
    '_',
    '*',
    '[',
    ']',
    '(',
    ')',
    '~',
    '`',
    '>',
    '#',
    '+',
    '-',
    '=',
    '|',
    '{',
    '}',
    '.',
    '!',
]


def markdown_free(text: str) -> str:
    for c in MDC:
        text = text.replace(c, f'\{c}')

    return text