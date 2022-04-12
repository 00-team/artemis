from json import load
from json import dump
from os.path import exists

from .config import BASE_DIR

CHATS_FILENAME = BASE_DIR / 'Bot/chats.json'


def update_chats(chats: list[str]):
    with open(CHATS_FILENAME, 'w') as f:
        return dump(chats, f)


def get_chats() -> list[str]:
    if not exists(CHATS_FILENAME):
        update_chats([])

    with open(CHATS_FILENAME, 'r') as f:
        return load(f)
