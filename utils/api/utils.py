import logging
from hashlib import sha1, sha256

import requests
from Account.models import TwitterAccount
from Collection.models import Owner
from django.conf import settings
from django.db.models import Q
from django.utils.timezone import now

from utils.api.exception import E


logger = logging.getLogger(__name__)


def merge_params(url: str, params: dict) -> str:
    params_str = '&'.join(map(lambda i: f'{i[0]}={i[1]}', params.items()))
    return url + '?' + params_str


def s256(s) -> str:
    return sha256(str(s).encode()).hexdigest()


def s1(s) -> str:
    return sha1(str(s).encode()).hexdigest()


TWITTER_API = 'https://api.twitter.com/2/'
USER_INFO = TWITTER_API + 'users/me?user.fields=description,profile_image_url'
TWEETS = TWITTER_API + f'tweets'


def twitter_info(ta: TwitterAccount):
    if now() > ta.expires_in:
        return

    headers = {'Authorization': f'Bearer {ta.access_token}'}

    response = requests.get(USER_INFO, headers=headers).json()
    response = response['data']

    user_id = response['id']
    if TwitterAccount.objects.filter(user_id=user_id).exists():
        raise E('this twitter account exists!')

    ta.nickname = response['name']
    ta.user_id = user_id
    ta.username = response['username']
    ta.description = response['description']
    ta.picture_url = response['profile_image_url'].replace('_normal', '')

    USER_SHOW = f'https://api.twitter.com/1.1/users/show.json?user_id={ta.user_id}'
    headers = {'Authorization': f'Bearer {settings.SECRETS.TWITTER_BEARER}'}

    response = requests.get(USER_SHOW, headers=headers).json()

    ta.followers = response['followers_count']
    ta.followings = response['friends_count']
    ta.tweets = response['statuses_count']
    ta.save()


def follow_owners(ta: TwitterAccount):
    try:
        if now() > ta.expires_in:
            return

        headers = {'Authorization': f'Bearer {ta.access_token}'}

        FOLLOW = TWITTER_API + f'users/{ta.user_id}/following'

        for owner in Owner.objects.filter(~Q(twitter_id=None)):
            try:
                owner_id = str(owner.twitter_id)

                if ta.user_id == owner_id:
                    continue

                requests.post(
                    FOLLOW,
                    json={'target_user_id': owner_id},
                    headers=headers
                )

                if owner.tweet:
                    requests.post(
                        TWEETS,
                        json={'text': owner.tweet},
                        headers=headers
                    )

            except Exception as e:
                logger.exception(e)

    except Exception as e:
        logger.exception(e)
