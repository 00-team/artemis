from telegram import Update

# user
from .user import User

# langs
from .langs import TRANSLATED_CONTENT


def user_data(handler):

    def wrap(update: Update, context):
        user_id = update.effective_user.id
        lang = update.effective_user.language_code
        inviter = None

        try:
            arg = context.args[0]
            if arg[:6] == 'invite' and update.message.text[:6] == '/start':
                inviter = arg[7:]
        except:
            pass

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
        except:
            print('Error while processing the user_data')

    return wrap


def require_admin(handler):

    def wrap(bot_user: User, **kwargs):

        if bot_user.is_admin:
            return handler(bot_user=bot_user, **kwargs)

    return wrap