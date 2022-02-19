# types
from telegram import Chat, Update
from telegram.ext import CallbackContext

# exceptions
from telegram.error import BadRequest, Unauthorized

# data
from .data import read_json, get_token
from .data import HOST

# user
from .user import user_by_id

# stages
from .stages import user_joined

# requests
import requests

admins = read_json('./data/main.json', {}).get('admins')
API_URL = HOST + 'api/bot/'

USER_PHOTO = 'AgACAgQAAxkBAAIB1mIQ-B9bGKi7MRGKh9Oqhwi1JWpkAALMuTEbwMCIUGuGyh16ARp-AQADAgADbQADIwQ'


def photo_info(update: Update, *args):
    user = update.effective_user

    if not user.id in admins:
        return

    photos = update.effective_message.photo
    chat = update.effective_chat

    for photo in photos:
        caption = f'''file id: `{photo.file_id}`\n\nfile size: `{photo.file_size}`\n\width: {photo.width}\t\theight: {photo.height}'''
        chat.send_photo(
            photo.file_id,
            caption=caption,
            parse_mode='MarkdownV2',
        )


def get_user_status(user_id) -> str | dict:
    BOT_SECRET = get_token()[1]

    headers = {'Authorization': BOT_SECRET}

    params = {'user_id': user_id}

    try:
        response = requests.get(
            API_URL + 'user_status/',
            params=params,
            headers=headers,
        )

        response = response.json()

        if response.get('error'):
            return response.get('error')

        return response
    except:
        return 'Error to get update from website'


def view_user(update: Update, context: CallbackContext):
    user_admin = update.effective_user
    bot = user_admin.bot

    if user_admin.id not in admins:
        return

    try:
        user_id = int(context.args[0])
    except:
        return user_admin.send_message(
            'use this command like this:\n'
            '/user <user-id:number>\n'
            '/user 12', )

    user_data = user_by_id(user_id)

    if not user_data:
        return user_admin.send_message(
            f'user with id {user_id} was not found!')

    try:
        user = bot.get_chat(user_id)
    except:
        return user_admin.send_message('Error to get this chat')

    # try:
    #     user.send_message('test message from admin')
    # except Unauthorized:
    #     return user_admin.send_message('bot was blocked by the user')

    # photo =

    def chats():
        not_joined = user_joined(user)

        if len(not_joined) == 0:
            return 'chats: Joined All ✅'

        chats_str = ', '.join(map(lambda c: f'`{c.title}`', not_joined))
        return f'chats: {chats_str}'

    user_status = get_user_status(user_id)
    if isinstance(user_status, dict):
        user_status = 'Loged in ✅'

    user_admin.send_photo(
        USER_PHOTO,
        f'{user.full_name}\n'
        f'username: {user.username}\n'
        f'bio: {user.bio}\n'
        f'lang: {user_data.lang}\n'
        f'invites: {user_data.total_invites}\n'
        f'{chats()}\n'
        f'site: {user_status}\n',
        parse_mode='MarkdownV2',
    )
