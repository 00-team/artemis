import logging
from collections.abc import Iterable
from threading import Thread
from time import sleep
from traceback import format_exception

from Account.models import Account, BotUser, TwitterAccount
from django.conf import settings
from django.utils.timezone import now
from requests import post

from .config import ACCOUNT, ACCOUNT_STATUS, BOT_USER, DEBUG_HOOK
from .config import DEFAULT_AVATAR as AVATAR
from .config import DEFAULT_USERNAME as USERNAME
from .config import HOST, HR, TWITTER_STATUS


logger = logging.getLogger(__name__)


def get_picture(url: None | str) -> str | None:
    if settings.DEBUG:
        return 'https://loremflickr.com/300/300'

    if url:
        return HOST + url


def date(d):
    return d.strftime('%Y-%m-%d %H:%M:%S')


def execute_hook(url: str, data: dict, timeout=0):
    try:
        if timeout:
            sleep(timeout)

        res = post(url, json=data)

        if res.status_code == 429:
            res = res.json()
            retry_after = int(res['retry_after'])
            return execute_hook(url, data, timeout=retry_after)

    except Exception as e:
        logger.exception(e)


def hook(url, embeds, username=USERNAME, avatar=AVATAR):
    data = {'username': username, 'avatar_url': avatar, 'embeds': embeds}

    if isinstance(url, str):
        Thread(target=execute_hook, args=(url, data)).start()

    elif isinstance(url, Iterable):
        for u in url:
            Thread(target=execute_hook, args=(u, data)).start()


def account_hook(account: Account, status: str):

    description = (
        f'**ID**: ||`{account.telegram_id}`||{HR}'
        f'**Wallet**: ||`{account.wallet}`||{HR}'
        f'**Join Date**: `{date(account.user.date_joined)}`{HR}'
        f'**Participated**: `{account.participated}`'
    )

    if account.username:
        description += f'{HR}**Link**: ||https://t.me/{account.username}||{HR}**Username**:||`{account.username}`||'

    color, author_name = ACCOUNT_STATUS[status]

    embed = {
        'title': account.nickname,
        'color': color,
        'timestamp': str(now()),
        'author': {
            'name': author_name
        },
        'description': description,
        'thumbnail': {
            'url': get_picture(account._picture)
        },
    }

    if status == 'delete':
        del embed['thumbnail']

    hook(ACCOUNT, [embed])


def twitter_hook(twitter: TwitterAccount, status: str):

    description = (f'**Account**: ||`{twitter.account.telegram_id}`||{HR}'
                   f'**ID**: ||`{twitter.user_id}`||{HR}'
                   f'**Username**: ||`{twitter.username}`||{HR}'
                   f'**Link**: ||https://twitter.com/{twitter.username}||{HR}'
                   f'**Followers**: `{twitter.followers}`\n'
                   f'**Followings**: `{twitter.followings}`\n'
                   f'**Tweets**: `{twitter.tweets}`{HR}')

    if twitter.description:
        description += f'**Bio**: \n{twitter.description}{HR}'

    color, author_name = TWITTER_STATUS[status]

    embed = {
        'title': twitter.nickname,
        'color': color,
        'timestamp': str(now()),
        'author': {
            'name': author_name
        },
        'description': description,
        'thumbnail': {
            'url': get_picture(twitter._picture)
        },
    }

    if status == 'disconnect':
        del embed['thumbnail']

    hook(ACCOUNT, [embed])


# 14811960 red error
def debug_hook(msg, title: str = 'Debug', color: int = 16766464):

    if isinstance(msg, BaseException):
        msg = ''.join(format_exception(msg))
    else:
        msg = str(msg)

    embed = {
        'title': title,
        'color': color,
        'timestamp': str(now()),
        'description': msg,
    }

    hook(DEBUG_HOOK, [embed])


def bot_user_hook(bot_user: BotUser):
    logged_in = False
    picture = None

    try:
        logged_in = bool(bot_user.account)
        picture = get_picture(bot_user.account._picture)
    except:
        pass

    def get_inviter():
        if bot_user.inviter:
            return f'||`{bot_user.inviter._fullname}` - `{bot_user.inviter.user_id}`||'

        return '`None`'

    description = (
        f'**User ID**: ||`{bot_user.user_id}`||{HR}'
        f'**Lang**: `{bot_user.lang}`{HR}'
        f'**Total Invites**: `{bot_user.total_invites}`{HR}'
        f'**Invites Counter**: `{bot_user.invites_counter}`{HR}'
        f'**Inviter**: {get_inviter()}{HR}'
        f'**Logged In**: `{logged_in}`{HR}'
    )

    embed = {
        'title': bot_user._fullname,
        'color': 2017768,
        'author': {
            'name': 'Bot User Update'
        },
        'timestamp': str(now()),
        'description': description,
        'thumbnail': {
            'url': picture
        }
    }

    hook(BOT_USER, [embed])
