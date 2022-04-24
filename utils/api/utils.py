# hash
from hashlib import sha256, sha1

# time
from django.utils.timezone import now

# models
from Account.models import TwitterAccount
from Collection.models import Owner

# filters
from django.db.models import Q

# conf
from django.conf import settings

# requests
import requests

# logger
import logging
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

    ta.nickname = response['name']
    ta.user_id = response['id']
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
