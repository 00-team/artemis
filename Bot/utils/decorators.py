# traceback
from traceback import print_exception

from telegram import Update, User as TelUser

# user
from .user import User

# langs
from .langs import TRANSLATED_CONTENT

# logger
import logging
logger = logging.getLogger(__name__)


def user_data(handler):
    def wrap(update: Update, context, *args, **kwargs):
        user = update.effective_user

        if not isinstance(user, TelUser):
            return

        if user.is_bot:
            return

        lang = user.language_code
        inviter = None

        try:
            arg = context.args[0]
            if arg[:6] == 'invite' and update.message.text[:6] == '/start':
                inviter = arg[7:]
        except:
            pass

        try:
            bot_user = User(
                user.id, inviter=inviter,
                lang=lang, fullname=user.full_name,
            )

            if lang not in TRANSLATED_CONTENT:
                lang = 'en'

            return handler(
                update=update,
                context=context,
                bot_user=bot_user,
                lang=lang,
            )
        except Exception as e:
            logger.exception(e)

    return wrap


def require_admin(handler):

    def wrap(bot_user: User, **kwargs):

        if bot_user.is_admin:
            return handler(bot_user=bot_user, **kwargs)

    return wrap
