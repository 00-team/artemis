from telegram import LoginUrl, Chat
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# conf
from .config import EXTERNAL_HOST

# langs
from .langs import CONTNET

LOGIN_URL = LoginUrl(EXTERNAL_HOST + '/api/account/telegram_callback/')


def help_keyboard(lang):
    cboard = CONTNET[lang]['help_keyboard']
    keyboard = list(
        map(
            lambda line: list(map(
                lambda b: InlineKeyboardButton(**b),
                line,
            )),
            cboard,
        ))
    return InlineKeyboardMarkup(keyboard)


def login_keyboard(lang):
    text = CONTNET[lang]['login_button']
    keyboard = [[InlineKeyboardButton(text, login_url=LOGIN_URL)]]

    return InlineKeyboardMarkup(keyboard)


def join_keyboard(chats: list[Chat], lang):
    text = text = CONTNET[lang]['chats_check_button']

    def GKB(c: Chat):
        return [InlineKeyboardButton(c.title, url=c.invite_link)]

    keyboard = list(map(GKB, chats)) + [[
        InlineKeyboardButton(text, callback_data='check_chats')
    ]]

    return InlineKeyboardMarkup(keyboard)


def invite_keyboard(link: str, lang):
    text = CONTNET[lang]['invite_button']
    keyboard = [[InlineKeyboardButton(text, url=link)]]

    return InlineKeyboardMarkup(keyboard)
