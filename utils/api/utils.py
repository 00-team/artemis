# hash
from hashlib import sha256

# time
from django.utils.timezone import now

# models
from Account.models import TwitterAccount


def merge_params(url: str, params: dict) -> str:
    params_str = '&'.join(map(lambda i: f'{i[0]}={i[1]}', params.items()))
    return url + '?' + params_str


def s256(s):
    return sha256(s.encode()).hexdigest()


def follow_owners(ta: TwitterAccount):
    try:
        if now() > ta.expires_in:
            return

        print(ta.access_token)

    except:
        pass