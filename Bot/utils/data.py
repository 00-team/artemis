from json import load
from json import dump
from os.path import exists

CHATS_FILENAME = './chats.json'


def update_chats(chats: list[str]):
    with open(CHATS_FILENAME, 'w') as f:
        return dump(chats, f)


def get_chats() -> list[str]:
    if not exists(CHATS_FILENAME):
        update_chats([])

    with open(CHATS_FILENAME, 'r') as f:
        return load(f)


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