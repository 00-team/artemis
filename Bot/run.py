# telegram api
from telegram import Update
from telegram.ext import Updater, Filters

# handlers
from telegram.ext import ChatMemberHandler, MessageHandler, CommandHandler
from telegram.ext import CallbackQueryHandler


# data
from utils.data import get_chats, update_chats

# conf
from utils.config import BOT_TOKEN, MODE

# lang
from utils.langs import COMMANDS

# decorators
from utils.decorators import user_data

# stages
from utils.sections import join_chats, update_join_chats
from utils.sections import invite, login, start
from utils.sections import help_cmd, help_callback

# admins
from utils.admin import photo_info, view_user, admin_help

# langs
from utils.langs import HELP_PATTERN

# logger
import logging
logging.basicConfig(
    filename='./bot.log',
    encoding='utf-8',
    level=logging.WARNING,
    format=(
        ('-' * 50) + '\n%(asctime)s\n'
        '%(levelname)s:%(name)s\n'
        '%(message)s\n'
    )
)
logger = logging.getLogger(__name__)


DEBUG = MODE == 'DEV'


@user_data
def member_update(update: Update, bot_user, **kwargs):
    try:
        user = update.effective_user
        chat = update.effective_chat
        chats = get_chats()

        if not bot_user.is_admin:
            return

        if chat.type not in ['supergroup', 'channel']:
            return

        status = update.my_chat_member.new_chat_member.status

        if status == 'administrator' and chat.id not in chats:
            chats.append(chat.id)
            user.send_message(
                f'chat: **{chat.title}** has been added into chats list',
                'Markdown')
        else:
            if chat.id in chats:
                chats.remove(chat.id)
                user.send_message(
                    f'chat: {chat.title} has been removed from chats list')

        update_chats(chats)
    except Exception as e:
        logger.error(e)


def main():
    try:
        updater = Updater(BOT_TOKEN)

        dp = updater.dispatcher

        # on bot added to a supergroup or channel as admin
        dp.add_handler(ChatMemberHandler(member_update))

        # commands
        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(CommandHandler('help', help_cmd))
        dp.add_handler(CommandHandler('login', login))
        dp.add_handler(CommandHandler('join', join_chats))
        dp.add_handler(CommandHandler('invite', invite))

        # admin commands
        dp.add_handler(CommandHandler('user', view_user))
        dp.add_handler(CommandHandler('admin', admin_help))

        dp.add_handler(
            CallbackQueryHandler(
                update_join_chats,
                pattern='check_chats',
            ))

        dp.add_handler(CallbackQueryHandler(
            help_callback,
            pattern=HELP_PATTERN,
        ))

        # photos
        dp.add_handler(MessageHandler(Filters.photo, photo_info))

        # help
        dp.add_handler(MessageHandler(Filters.text('help'), help_cmd))

        if not DEBUG:
            for lang_code, commands in COMMANDS:
                updater.bot.set_my_commands(commands, language_code=lang_code)

        updater.start_polling()
        print('started!')
        updater.idle()
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    main()
