
from telegram import Chat, Update
from telegram.error import BadRequest, Unauthorized

from .config import get_photo
from .data import get_chats, update_chats
from .decorators import user_data
from .keyboards import help_keyboard, invite_keyboard, join_keyboard
from .keyboards import login_keyboard
from .langs import CONTNET, TRANSLATED_CONTENT
from .logger import get_logger
from .user import User


logger = get_logger(__name__)


@user_data
def login(update: Update, lang, **kwargs):
    try:
        chat = update.effective_chat

        chat.send_message(
            CONTNET[lang]['login'],
            reply_markup=login_keyboard(lang),
        )
    except Unauthorized:
        pass


def user_not_joined(user: Chat) -> list[Chat]:
    '''
    return list of chats that user need to join 
    e.g. chats that user not joined into them.
    '''
    chats = get_chats()
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
            update_chats(chats)
        except BadRequest:
            chats.remove(chat)
            update_chats(chats)

    return user_chats


def check_inviter(update: Update, bot_user: User):
    if not bot_user.inviter or bot_user.invites_counter:
        return

    the_bot = update.effective_user.bot

    try:
        inviter_id = bot_user.inviter.user_id
        inviter_user = the_bot.get_chat_member(inviter_id, inviter_id).user
        inviter_lang = inviter_user.language_code

        if inviter_lang not in TRANSLATED_CONTENT:
            inviter_lang = 'en'

        if user_not_joined(inviter_user):
            bot_user.update_inviter(increase=False)

            unsuccess_invite = CONTNET[inviter_lang]['unsuccess_invite']
            inviter_user.send_message(unsuccess_invite)

            return

        bot_user.update_inviter()

        inviter_user.send_message(CONTNET[inviter_lang]['success_invite'])

    except Unauthorized:
        pass

    except Exception as e:
        logger.exception(e)


@user_data
def join_chats(update: Update, bot_user, lang, **kwargs):
    try:
        user = update.effective_user
        user_chats = user_not_joined(user)
        chat = update.effective_chat

        if user_chats:
            chat.send_photo(
                get_photo(),
                caption=CONTNET[lang]['join_chats'],
                reply_markup=join_keyboard(user_chats, lang),
            )

            return

        check_inviter(update, bot_user)
        chat.send_photo(
            get_photo(),
            caption=CONTNET[lang]['joined_chats'],
        )
    except Unauthorized:
        pass


@user_data
def update_join_chats(update: Update, bot_user, lang, **kwargs):
    query = update.callback_query
    user = update.effective_user
    user_chats = user_not_joined(user)

    if user_chats:
        try:
            query.message.edit_caption(
                CONTNET[lang]['join_incomplete'],
                reply_markup=join_keyboard(user_chats, lang),
            )
        except BadRequest:
            pass
        except Unauthorized:
            pass

        return

    check_inviter(update, bot_user)

    try:
        query.message.edit_caption(
            CONTNET[lang]['join_complete'],
            reply_markup=None,
        )
    except BadRequest:
        pass
    except Unauthorized:
        pass


@user_data
def invite(update: Update, bot_user: User, lang, **kwargs):
    try:
        user = update.effective_user
        chat = update.effective_chat
        bot_username = user.bot.username
        enough_invites = bot_user.total_invites >= 10

        user_link = f'https://t.me/{bot_username}?start=invite-{bot_user.invite_hash}'

        text = CONTNET[lang]['invites']
        text = text.format(user_link, bot_user.total_invites)

        user.send_message(text)

        user.send_photo(
            get_photo(),
            CONTNET[lang]['invite_banner'],
            reply_markup=invite_keyboard(user_link, lang),
        )

        if enough_invites:
            chat.send_message(CONTNET[lang]['enough_invites'])

    except Unauthorized:
        pass


@user_data
def start(update: Update, context, lang, **kwargs):
    try:
        user = update.effective_user

        user.send_message(CONTNET[lang]['start'])
        user.send_message(CONTNET[lang]['help'],
                          reply_markup=help_keyboard(lang))

        try:
            arg = context.args[0]

            if arg == 'login':
                user.send_message(
                    CONTNET[lang]['external_login'],
                    reply_markup=login_keyboard(lang),
                )

        except Exception:
            pass

    except Unauthorized:
        pass


@user_data
def help_cmd(update: Update, lang, **kwargs):
    try:
        user = update.effective_user
        user.send_message(CONTNET[lang]['help'],
                          reply_markup=help_keyboard(lang))
    except Unauthorized:
        pass


@user_data
def help_callback(update: Update, lang, **kwrags):
    query = update.callback_query

    try:
        query.message.edit_text(
            CONTNET[lang]['help_edit'],
            reply_markup=None
        )
    except BadRequest:
        pass
    except Unauthorized:
        pass

    match query.data[5:]:
        case 'join':
            join_chats(update=update, **kwrags)
        case 'invite':
            invite(update=update, **kwrags)
        case 'login':
            login(update=update, **kwrags)
        case _:
            return


@user_data
def wallet(update: Update, lang, bot_user, **kwargs):
    try:
        no_wallet = CONTNET[lang]['no_wallet']
        text = CONTNET[lang]['wallet'].format(bot_user.wallet or no_wallet)
        update.effective_user.send_message(
            text,
            reply_markup=login_keyboard(lang, 'edit_wallet')
        )
    except Unauthorized:
        pass
