from typing import Literal

# requests
import requests

# conf
from .config import HEADERS, INTERNAL_HOST

HOST = INTERNAL_HOST + '/api/bot/'


class Inviter:
    user_id: int
    invite_hash: str
    total_invites: int

    def __init__(self, obj):
        self.user_id = obj['user_id']
        self.invite_hash = obj['invite_hash']
        self.total_invites = obj['total_invites']


class User:
    LANG = Literal['EN', 'RU']

    user_id: int
    is_admin: bool
    lang: LANG
    invite_hash: str
    total_invites: int
    invites_counter: bool
    inviter: Inviter | None = None
    exists: bool

    def __init__(self, user_id, inviter=None, lang='en', fullname=None):
        self.user_id = user_id
        params = {
            'user_id': self.user_id, 'lang': lang,
            'fullname': fullname,
        }

        if inviter:
            params['inviter'] = inviter

        self.get_user(params)

    def get_user(self, params):

        res = requests.get(
            HOST + 'get_bot_user/',
            params=params,
            headers=HEADERS,
        )

        if res.status_code != 200:
            raise

        res = res.json()

        self.is_admin = res['is_admin']
        self.lang = res['lang']
        self.invite_hash = res['invite_hash']
        self.total_invites = res['total_invites']
        self.invites_counter = res['invites_counter']
        self.exists = res['exists']

        if res['inviter']:
            self.inviter = Inviter(res['inviter'])

    def update_inviter(self, increase: bool = True):
        params = {'user_id': self.user_id}

        if increase:
            params['increase'] = 'true'

        requests.get(
            HOST + 'update_inviter/',
            params=params,
            headers=HEADERS,
        )
