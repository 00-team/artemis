# types
from telegram import Update
from telegram.ext import CallbackContext

# decorators
from .decorators import user_data, require_admin

# data
from .data import markdown_free

# stages
from .stages import user_joined


@user_data
@require_admin
def photo_info(update: Update, **kwargs):
    photos = update.effective_message.photo
    chat = update.effective_chat

    for photo in photos:
        caption = (f'file id: \n`{photo.file_id}`\n\n'
                   f'file size: `{photo.file_size // 1000} KB`\n'
                   f'width: {photo.width}\n'
                   f'height: {photo.height}')
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
            '/user 12', )

    try:
        user = bot.get_chat(user_id)
    except:
        return user_admin.send_message('Error to get this chat')

    def chats():
        not_joined = user_joined(user)

        if len(not_joined) == 0:
            return 'chats: Joined All ✅'

        chats_str = ', '.join(
            map(lambda c: f'`{markdown_free(c.title)}`', not_joined))
        return f'chats: {chats_str}'

    fname = markdown_free(f'full name: {user.full_name}')
    uname = f'username: [{user.username}]({user.link})'
    bio = markdown_free(f'bio: {user.bio}')

    uchats = chats()

    text = '\n'.join((fname, uname, bio, uchats))

    user_admin.send_message(text, parse_mode='MarkdownV2')


@user_data
@require_admin
def admin_help(update: Update, **kwargs):
    chat = update.effective_chat
    text = ('/user <user:id> - for viewing the users\n'
            '/admin - for showing this message\n'
            'sending or forwarding a photo - getting info about that photo')
    chat.send_message(text)
