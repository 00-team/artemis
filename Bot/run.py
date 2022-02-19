# telegram api
from telegram import Update
from telegram.ext import Updater, Filters

# handlers
from telegram.ext import ChatMemberHandler, MessageHandler, CommandHandler
from telegram.ext import CallbackQueryHandler, CallbackContext

# user
from utils.user import User

# data
from utils.data import update_data
from utils.data import get_token, read_json

# stages
from utils.stages import join_chats, update_join_chats
from utils.stages import login, invite, check_invite

# admins
from utils.admin import photo_info, view_user

# langs
from utils.langs import change_lang, update_lang

# logger
from logging import getLogger

logger = getLogger(__name__)

data = read_json('./data/main.json', {})
admins = data.get('admins')
chats = data.get('chats')
del data


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    user_data = User(user.id)

    try:
        arg = context.args[0]

        if arg == 'login':
            return login(update)

        if arg[:6] == 'invite' and not user_data.user_exists:
            check_invite(update, arg[7:], user_data)
    except:
        pass

    if not user_data.user_exists:
        return change_lang(update, next_step=True)

    join_chats(update)


def member_update(update: Update, *args):
    try:
        user = update.effective_user
        chat = update.effective_chat

        if not user.id in admins:
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

        update_data(chats)
    except Exception as e:
        logger.error(e)


def main():

    updater = Updater(get_token()[0])

    dp = updater.dispatcher

    # on bot added to a supergroup or channel as admin
    dp.add_handler(ChatMemberHandler(member_update))

    # commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler(['lang', 'language'], change_lang))
    dp.add_handler(CommandHandler('login', login))
    dp.add_handler(CommandHandler('join', join_chats))
    dp.add_handler(CommandHandler('invite', invite))

    # admin commands
    dp.add_handler(CommandHandler('user', view_user))

    # callbacks
    dp.add_handler(
        CallbackQueryHandler(
            update_lang,
            pattern='(next_|)(en|ru)',
        ))
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