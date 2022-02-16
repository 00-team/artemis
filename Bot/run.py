from json import loads

# telegram api
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LoginUrl
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, *args):
    # print(dir(update))
    login_url = LoginUrl('https://web-00-team.web.app/')
    keyboard = [
        [
            InlineKeyboardButton('Login', login_url=login_url),
        ],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    # update.message.connected_website = 'http://localhost:7000/'

    update.message.reply_text(f'Hello {update.effective_user.first_name}',
                              reply_markup=markup)


def get_token() -> str:
    with open('../secrets.json', 'r') as f:
        return loads(f.read())['BOT_TOKEN']


def main():
    updater = Updater(get_token())

    updater.dispatcher.add_handler(CommandHandler('start', hello))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()