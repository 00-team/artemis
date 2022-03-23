# telegram api
from telegram import Update
from telegram.ext import Updater, Filters

# handlers
from telegram.ext import ChatMemberHandler, MessageHandler, CommandHandler
from telegram.ext import CallbackQueryHandler

# data
from utils.data import get_chats, update_chats

# conf
from utils.config import BOT_TOKEN

# stages
from utils.stages import join_chats, update_join_chats
from utils.stages import login, invite
from utils.stages import login_markup

# admins
from utils.admin import photo_info, view_user

# langs
from utils.langs import CONTNET

# logger
from logging import getLogger

# decorators
from utils.decorators import user_data

# user
from utils.user import User

logger = getLogger(__name__)


@user_data
def start(update: Update, context, lang, **kwargs):

    user = update.effective_user

    user.send_message(CONTNET[lang]['start'])
    user.send_message(CONTNET[lang]['help'])

    try:
        arg = context.args[0]

        if arg == 'login':
            user.send_message(
                CONTNET[lang]['external_login'],
                reply_markup=login_markup(lang),
            )

    except:
        pass


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

    updater = Updater(BOT_TOKEN)

    dp = updater.dispatcher

    # on bot added to a supergroup or channel as admin
    dp.add_handler(ChatMemberHandler(member_update))

    # commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('login', login))
    dp.add_handler(CommandHandler('join', join_chats))
    dp.add_handler(CommandHandler('invite', invite))

    # admin commands
    dp.add_handler(CommandHandler('user', view_user))

    dp.add_handler(
        CallbackQueryHandler(
            update_join_chats,
            pattern='check_chats',
        ))

    # photos
    dp.add_handler(MessageHandler(Filters.photo, photo_info))

    updater.start_polling()
    print('started!')
    updater.idle()


if __name__ == '__main__':
    main()