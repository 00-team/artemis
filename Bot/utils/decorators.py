from telegram import Update

# user
from .user import User

# langs
from .langs import TRANSLATED_CONTENT


def user_data(handler):

    def wrap(update: Update, context):
        user_id = update.effective_user.id
        lang = update.effective_user.language_code

        try:
            arg = context.args[0]
            if arg[:6] == 'invite':
                inviter = arg[7:]
        except:
            inviter = None

        try:
            bot_user = User(user_id, inviter=inviter, lang=lang)

            if lang not in TRANSLATED_CONTENT:
                lang = 'en'

            return handler(
                update=update,
                context=context,
                bot_user=bot_user,
                lang=lang,
            )
        except Exception as e:
            print('Error while processing the user_data')

    return wrap