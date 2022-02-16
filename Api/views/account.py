from django.http import HttpRequest, HttpResponseRedirect, JsonResponse

# requests
from requests import post

# messages
from django.contrib import messages

# auth
from django.contrib.auth import logout as system_logout
from django.contrib.auth import login as system_login

# execptions
from utils.api import E

# utils
from utils.api import HOST, get_data
from utils.api import validate_telegram_data
# django
from django.utils.crypto import get_random_string

# models
from Account.models import Account


def twitter_auth(request: HttpRequest):
    try:
        host = HOST(request)
        url = 'https://twitter.com/i/oauth2/authorize?response_type=code'
        url += '&client_id=MjRXdnA1WV9PLUVRamM4UUVOamw6MTpjaQ'
        url += f'&redirect_uri={host}api/twitter_callback/'
        url += '&scope=users.read+follows.read+follows.write'
        url += f'&state={get_random_string(30)}'
        url += f'&code_challenge={get_random_string(30)}'
        url += '&code_challenge_method=plain'

        # return HttpResponseRedirect(url)
        return JsonResponse({'url': url})
    except E as e:
        return e.response


def twitter_callback(request: HttpRequest):
    return JsonResponse({})


def telegram_callback(request: HttpRequest):
    try:
        data = get_data(request)
        validate_telegram_data(data.copy())
        system_logout(request)

        submit_data = {
            'telegram_id': int(data.get('id')),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'username': data.get('username'),
            'photo_url': data.get('photo_url'),
        }

        account = Account.objects.submit(**submit_data)

        system_login(request, account.user)

        return HttpResponseRedirect('/account/')
    except E as e:
        messages.error(request, e.message)
        return HttpResponseRedirect('/')


def logout(request: HttpRequest):
    system_logout(request)
    return HttpResponseRedirect('/')