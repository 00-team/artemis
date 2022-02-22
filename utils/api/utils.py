# hash
from hashlib import sha256

# time
from django.utils.timezone import now

# models
from Account.models import TwitterAccount
from Collection.models import Owner

# filters
from django.db.models import Q

# requests
import requests


def merge_params(url: str, params: dict) -> str:
    params_str = '&'.join(map(lambda i: f'{i[0]}={i[1]}', params.items()))
    return url + '?' + params_str


def s256(s):
    return sha256(s.encode()).hexdigest()


USER_INFO = 'https://api.twitter.com/2/users/me'


def follow_owners(ta: TwitterAccount):
    try:
        if now() > ta.expires_in:
            return

        headers = {'Authorization': f'Bearer {ta.access_token}'}

        response = requests.get(USER_INFO, headers=headers)
        response = response.json()['data']
        ta.username = response['username']
        user_id = response['id']

        FOLLOW = f'https://api.twitter.com/2/users/{user_id}/following'

        for owner in Owner.objects.filter(~Q(twitter_id=None)):
            try:
                json = {'target_user_id': str(owner.twitter_id)}

                requests.post(FOLLOW, json=json, headers=headers)

            except:
                pass

        ta.save()

    except:
        pass