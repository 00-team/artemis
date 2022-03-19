from time import sleep
from requests import post
from django.utils.timezone import now

from threading import Thread

from utils.models.user import username

from collections.abc import Iterable

# configs
from .config import HOST, ACCOUNT
from .config import DEFAULT_USERNAME as USERNAME
from .config import DEFAULT_AVATAR as AVATAR
from .config import HR
from .config import ACCOUNT_STATUS, TWITTER_STATUS

from django.conf import settings

# modeles
from Account.models import Account, TwitterAccount

queue = []
checking = False


def get_picture(url: None | str) -> str | None:
    if settings.DEBUG:
        return 'https://loremflickr.com/300/300'
    elif url:
        return HOST + url


def date(d):
    return d.strftime('%Y-%m-%d %H:%M:%S')


def check_queue():
    global checking, queue
    checking = True

    for r in queue:
        try:
            post(r['url'], json=r['data'])
            sleep(.5)
        except:
            print('Error while sending webhook ...')

    queue = []
    checking = False


def hook(url, embeds, username=USERNAME, avatar=AVATAR):
    data = {'username': username, 'avatar_url': avatar, 'embeds': embeds}

    if isinstance(url, str):
        queue.append({'url': url, 'data': data})

    elif isinstance(url, Iterable):
        for u in url:
            queue.append({'url': u, 'data': data})

    if not checking:
        Thread(target=check_queue).start()


def account_hook(account: Account, status: str):

    description = f'''**ID**: `{account.telegram_id}`{HR}**Wallet**: `{account.wallet}`{HR}**Join Date**: `{date(account.user.date_joined)}`'''

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


def twitter_hook(account: TwitterAccount, status: str):

    description = f'''**ID**: `{account.telegram_id}`{HR}**Wallet**: `{account.wallet}`{HR}**Join Date**: `{date(account.user.date_joined)}`'''

    if account.username:
        description += f'{HR}**Link**: ||https://t.me/{account.username}||{HR}**Username**:||`{account.username}`||'

    color, author_name = TWITTER_STATUS[status]

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
