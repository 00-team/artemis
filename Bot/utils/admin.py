# types
from telegram import Update
from telegram.ext import CallbackContext

# decorators
from .decorators import user_data, require_admin


# stages
from .sections import user_not_joined


@user_data
@require_admin
def photo_info(update: Update, **kwargs):
    photos = update.effective_message.photo
    chat = update.effective_chat

    photo = None

    for p in photos:
        if not photo:
            photo = p
            continue

        if photo.file_size < p.file_size:
            photo = p

    caption = (
        f'file id: \n`{photo.file_id}`\n\n'
        f'file size: `{photo.file_size // 1000} KB`\n'
        f'width: {photo.width}\n'
        f'height: {photo.height}'
    )
    chat.send_photo(
        photo.file_id,
        caption=caption,
        parse_mode='MarkdownV2',
    )


@user_data
@require_admin
def view_user(update: Update, context: CallbackContext, **kwargs):
    user_admin = update.effective_user
    bot = user_admin.bot

    try:
        user_id = int(context.args[0])
    except:
        return user_admin.send_message(
            'use this command like this:\n'
            '/user <user-id:number>\n'
            '/user 12'
        )

    try:
        user = bot.get_chat(user_id)
    except:
        return user_admin.send_message('Error to get this chat')

    def chats():
        not_joined = user_not_joined(user)

        if not not_joined:
            return 'chats: joined all ✅'

        chats_str = '\n'.join(map(lambda c: f'{c.title}', not_joined))
        return (
            '---------- chats that user need to join ----------\n'
            f'{chats_str}'
            '\n' + '-' * 62
        )

    text = f'full name: {user.full_name}\n'

    if user.username:
        text += f'username: {user.username}\n{user.link}\n'

    if user.bio:
        text += ('---------- bio ----------\n'
                 f'{user.bio}'
                 '\n--------------------------\n')

    text += chats()
    user_admin.send_message(text)


@user_data
@require_admin
def admin_help(update: Update, **kwargs):
    chat = update.effective_chat
    text = (
        '/user <user:id> - for viewing the users\n'
        '/admin - for showing this message\n'
        'sending or forwarding a photo - getting info about that photo'
    )
    chat.send_message(text)
