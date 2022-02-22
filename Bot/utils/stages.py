# types
from telegram import Chat, Update, LoginUrl
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# exceptions
from telegram.error import BadRequest, Unauthorized

from .data import markdown_free, update_data, HOST, get_date
from .user import User, user_by_invite
from .langs import langs, user_lang

JOIN_PHOTO = 'AgACAgQAAxkBAAICT2IUoWhe2dqMs5JH4KQOsVUIYBXnAAJWuTEbX9OgUMou1QABxjrs5wEAAwIAA20AAyME'
INVITE_PHOTO = 'AgACAgQAAxkBAAICjWIUvJR2Ij73vIEeNU4VHJaH_JVDAALUtzEbTt2oUH7o1bYu7AtdAQADAgADeQADIwQ'
LOGIN_URL = LoginUrl(HOST + 'api/account/telegram_callback/')


def login_markup(lang):
    text = 'Login!'

    if lang == 'ru':
        text = 'Авторизоваться!'

    keyboard = [[InlineKeyboardButton(text, login_url=LOGIN_URL)]]

    return InlineKeyboardMarkup(keyboard)


def login(update: Update, *args):
    chat = update.effective_chat
    user_data = User(update.effective_user.id)

    chat.send_message(
        langs['login'][user_data.lang],
        reply_markup=login_markup(user_data.lang),
    )


def user_joined(user: Chat) -> list[Chat]:
    chats = get_date()['chats']
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


def join_markup(chats: list[Chat], lang):
    text = 'check ✅'

    if lang == 'ru':
        text = 'чек об оплате ✅'

    def GKB(c: Chat):
        return [InlineKeyboardButton(c.title, url=c.invite_link)]

    keyboard = list(map(GKB, chats)) + [[
        InlineKeyboardButton(text, callback_data='check_chats')
    ]]

    return InlineKeyboardMarkup(keyboard)


def join_chats(update: Update, *args):
    user = update.effective_user
    user_chats = user_joined(user)
    chat = update.effective_chat

    lang = user_lang(user.id)

    if user_chats:
        return chat.send_photo(
            JOIN_PHOTO,
            caption=langs['join_chats'][lang],
            reply_markup=join_markup(user_chats, lang),
        )

    invite(update)


def update_join_chats(update: Update, *args):
    query = update.callback_query
    user = update.effective_user
    user_chats = user_joined(user)
    lang = user_lang(user.id)

    if user_chats:
        return

    query.message.edit_caption(
        langs['join_complete'][lang],
        reply_markup=None,
    )

    invite(update)


def update_lang(update: Update, *args):
    user = update.effective_user
    chat = update.effective_chat
    query = update.callback_query
    next_step = False
    ln = query.data

    if ln[:4] == 'next':
        next_step = True
        ln = ln[5:]

    user_data = User(user.id)
    user_data.update(lang=ln)

    query.message.edit_text(
        langs['lang_updated'][user_data.lang],
        reply_markup=None,
        parse_mode='MarkdownV2',
    )

    if next_step:
        join_chats(update)


def invite_markup(link: str, lang):
    text = 'To get NFT enter the robot ✅'
    if lang == 'ru':
        text = 'Войдите, чтобы получить NFT ✅'
    keyboard = [[InlineKeyboardButton(text, url=link)]]

    return InlineKeyboardMarkup(keyboard)


def invite(update: Update, *args):
    user = update.effective_user
    chat = update.effective_chat
    bot_username = user.bot.username
    user_data = User(user.id)
    enough_invites = user_data.total_invites >= 3

    user_link = f'https://t.me/{bot_username}?start=invite-{user_data.invite}'

    text = (f'\n[Your Link]({user_link})\n'
            f'Your total invites: {user_data.total_invites}/3')

    if user_data.lang == 'ru':
        text = (f'\n[Ваша ссылка]({user_link})\n'
                f'Всего приглашений: {user_data.total_invites}/3')

    user.send_message(
        markdown_free(langs['invites'][user_data.lang]) + text,
        parse_mode='MarkdownV2',
    )

    user.send_photo(
        INVITE_PHOTO,
        langs['invite_banner'][user_data.lang],
        reply_markup=invite_markup(user_link, user_data.lang),
    )

    if enough_invites:
        chat.send_message(langs['enough_invites'][user_data.lang])

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

    total_invites = inviter.total_invites + 1

    inviter.update(total_invites=total_invites)
    bot.send_message(inviter.user_id, langs['success_invite'][inviter.lang])

    if total_invites >= 3:
        bot.send_message(
            inviter.user_id,
            langs['enough_invites'][inviter.lang],
        )
        bot.send_message(
            inviter.user_id,
            langs['login'][inviter.lang],
            reply_markup=login_markup(inviter.lang),
        )
