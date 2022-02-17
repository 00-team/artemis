from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .data import update_users
from .api import join_chats

langs = {
    'welcome': {
        'en': '🌀 Welcome to the Artemis Bot',
        'ru': '🌀 Добро пожаловать в бота Artemis',
    },
    'choose_lang': {
        'en': '🇺🇸 Please select your language',
        'ru': '🇷🇺 Пожалуйста, выберите ваш язык',
    },
    'lang': {
        'en': '🇺🇸 English',
        'ru': '🇷🇺 Pусский',
    },
    'lang_updated': {
        'en': 'Your Language has been *Successfully* Updated\!',
        'ru': 'Ваш язык успешно обновлен',
    }
}


def lang_markup(next_step=False):
    en = 'en'
    ru = 'ru'
    if next_step:
        en = 'next_en'
        ru = 'next_ru'

    lang_keyboard = [
        [
            InlineKeyboardButton(langs['lang']['en'], callback_data=en),
            InlineKeyboardButton(langs['lang']['ru'], callback_data=ru),
        ],
    ]
    return InlineKeyboardMarkup(lang_keyboard)


choose_lang_msg = f'''
{langs['welcome']['en']}
{langs['welcome']['ru']}

    {langs['choose_lang']['en']}
    {langs['choose_lang']['ru']}
'''


def change_lang(update: Update, *args, next_step=False):
    chat = update.effective_chat
    chat.send_message(choose_lang_msg, reply_markup=lang_markup(next_step))


def update_lang(update: Update, *args):
    user = update.effective_user
    chat = update.effective_chat
    query = update.callback_query
    next_step = False
    ln = 'en'
    if query.data[:4] == 'next':
        next_step = True
        ln = query.data[5:]

    update_users(user.id, ln)

    query.message.edit_text(
        langs['lang_updated'][ln],
        reply_markup=None,
        parse_mode='MarkdownV2',
    )

    if next_step:
        join_chats(update)
