# types
from telegram import Chat, Update, LoginUrl
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# exceptions
from telegram.error import BadRequest, Unauthorized

from .data import update_data, read_json
from .user import User, user_by_invite

JOIN_PHOTO = 'AgACAgQAAxkBAAP1Yg6vVJoia905Dxb0SvOwTylzTAoAAs61MRvJ83FQIfIOlaPnPVsBAAMCAANtAAMjBA'
LOGIN_URL = LoginUrl('http://127.0.0.1:7000/api/account/telegram_callback/')


def login(update: Update, *args):
    chat = update.effective_chat

    keyboard = [[InlineKeyboardButton('Login!', login_url=LOGIN_URL)]]

    markup = InlineKeyboardMarkup(keyboard)
    chat.send_message(
        'make a account in our website and give us your wallet addr so we can send you the token',
        reply_markup=markup)


def user_joined(user: Chat) -> list[Chat]:
    chats = read_json('./data/main.json')['chats']
    bot = user.bot
    user_chats = []

    for chat in chats:
        try:
            res = bot.get_chat_member(chat, user.id)
            if res.status in ['left', 'kicked']:
                chat = bot.get_chat(chat)
                user_chats.append(chat)
        except Unauthorized:
            chats.remove(chat)
            update_data(chats)
        except BadRequest:
            chats.remove(chat)
            update_data(chats)

    return user_chats


def join_markup(chats: list[Chat]):

    def GKB(c: Chat):
        return [InlineKeyboardButton(c.title, url=c.invite_link)]

    keyboard = list(map(GKB, chats)) + [[
        InlineKeyboardButton('check!', callback_data='check_chats')
    ]]

    return InlineKeyboardMarkup(keyboard)


def join_chats(update: Update, *args):
    user_chats = user_joined(update.effective_user)
    chat = update.effective_chat

    if user_chats:
        return chat.send_photo(
            JOIN_PHOTO,
            caption='the caption ...',
            reply_markup=join_markup(user_chats),
        )

    invite(update)


def update_join_chats(update: Update, *args):
    query = update.callback_query

    user_chats = user_joined(update.effective_user)

    if user_chats:
        return query.message.edit_caption(
            'gg caption',
            reply_markup=join_markup(user_chats),
            parse_mode='MarkdownV2',
        )

    query.message.edit_caption(
        'yooo you did it',
        reply_markup=None,
        parse_mode='MarkdownV2',
    )

    invite(update)


def invite_markup(link: str):
    keyboard = [[InlineKeyboardButton('start the bot now gg', url=link)]]

    return InlineKeyboardMarkup(keyboard)


def invite(update: Update, *args):
    user = update.effective_user
    chat = update.effective_chat
    bot_username = user.bot.username
    user_data = User(user.id)
    enough_invites = user_data.total_invites >= 1

    user_link = f't.me/{bot_username}?start=invite-{user_data.invite}'

    user.send_message(f'''
        Your invite Link: {user_link} \n Your invites: {user_data.total_invites}'''
                      )
    user.send_message(
        'makeing a banner for this user',
        reply_markup=invite_markup(user_link),
    )

    if enough_invites:
        chat.send_message('yooo you just invite enough member to the bot')

        login(update)


def check_invite(update: Update, invite_hash: str, user_data: User):
    user = update.effective_user
    bot = user.bot
    inviter = user_by_invite(invite_hash)

    # make sure invite url is valid
    if not inviter:
        return

    # make sure user doesn't invite him self
    if user_data.user_id == inviter.user_id:
        return

    inviter.update(total_invites=inviter.total_invites + 1)
    bot.send_message(
        inviter.user_id,
        f'gg user {user.first_name} has been invited with your link')
