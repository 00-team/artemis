
from telegram import Update
from telegram.ext import CallbackQueryHandler, ChatMemberHandler
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from utils.admin import admin_help, photo_info, view_user
from utils.config import BOT_TOKEN, MODE
from utils.data import get_chats, update_chats
from utils.decorators import user_data
from utils.langs import COMMANDS, HELP_PATTERN
from utils.logger import get_logger
from utils.sections import help_callback, help_cmd, invite, join_chats, login
from utils.sections import start, update_join_chats, wallet


logger = get_logger(__name__)


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
        logger.exception(e)


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
        dp.add_handler(CommandHandler('wallet', wallet))

        # admin commands
        dp.add_handler(CommandHandler(['user', 'u'], view_user))
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
