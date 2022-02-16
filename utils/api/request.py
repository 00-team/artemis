# types
from django.http import HttpRequest

# utils
from json import loads as json_loads
from hashlib import sha256
import hmac
from time import time

# confings
from django.conf import settings

# exceptions
from .exception import E


def HOST(request: HttpRequest) -> str:
    return f'{request.scheme}://{request.get_host()}/'


def BodyLoader(body: bytes) -> dict:
    try:
        return json_loads(body)
    except Exception:
        return {}


def get_data(request: HttpRequest) -> dict:
    data = {}

    if request.method == 'GET':
        if request.GET:
            data = request.GET
        elif request.content_type != 'multipart/form-data':
            data = BodyLoader(request.body)

    elif request.method == 'POST':
        if request.POST:
            data = request.POST
        elif request.content_type != 'multipart/form-data':
            data = BodyLoader(request.body)

    if not isinstance(data, dict):
        data = {}

    return data


def validate_telegram_data(data: dict):
    try:

        data_hash = data.get('hash')
        auth_date = int(data.get('auth_date'))
        now_date = int(time())

        if now_date - auth_date > 86400:
            raise

        data.pop('hash')

        data_list = list(map(lambda i: f'{i[0]}={i[1]}', data.items()))
        data_list.sort()

        data_message = '\n'.join(data_list).encode()

        token = sha256(settings.BOT_TOKEN.encode()).digest()

        hashed = hmac.new(token, msg=data_message, digestmod=sha256)
        hashed = hashed.hexdigest()

        if hashed != data_hash:
            raise E('Login is not valid')

    except E as e:
        raise e

    except Exception:
        raise E
