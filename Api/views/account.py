from django.http import HttpRequest, HttpResponseRedirect, JsonResponse

# requests
from requests import post

# messages
from django.contrib import messages

# time
from django.utils.timezone import now
from datetime import timedelta

# auth
from django.contrib.auth import logout as system_logout
from django.contrib.auth import login as system_login

# decorators
from django.views.decorators.http import require_GET, require_POST
from Api.decorators import login_required

# csrf
from django.middleware.csrf import get_token

# execptions
from utils.api import E

# conf
from django.conf import settings

# utils
from utils.api import HOST, get_data
from utils.api import validate_telegram_data
from utils.api import merge_params, follow_owners
from utils.api import twitter_info
# django
from django.utils.crypto import get_random_string as random_str

# models
from Account.models import Account, BotUser, TwitterAccount

# hreading
from threading import Thread

# logger
import logging
logger = logging.getLogger(__name__)


AUTH_BASE_URL = 'https://twitter.com/i/oauth2/authorize'
ACCESS_TOKEN_URL = 'https://api.twitter.com/2/oauth2/token'


@require_GET
@login_required()
def twitter_auth(request: HttpRequest):
    try:
        session = request.session
        state = random_str(30)
        code_challenge = random_str(30)
        host = HOST(request)

        session['state'] = state
        session['code_challenge'] = code_challenge

        scopes = [
            'users.read', 'follows.read', 'follows.write',
            'tweet.read', 'tweet.write'
        ]

        params = {
            'response_type': 'code',
            'client_id': settings.SECRETS.CLIENT_ID,
            'redirect_uri': f'{host}api/account/twitter_callback/',
            'scope': '+'.join(scopes),
            'state': state,
            'code_challenge': code_challenge,
            'code_challenge_method': 'plain',
        }

        url = merge_params(AUTH_BASE_URL, params)

        return HttpResponseRedirect(url)
    except E as e:
        messages.error(request, e.message)
        return HttpResponseRedirect('/')


@require_GET
@login_required()
def twitter_callback(request: HttpRequest):
    try:
        session = request.session
        account = request.user.account

        data = get_data(request)
        host = HOST(request)
        code = data.get('code')
        state = data.get('state')

        session_state = session.get('state')
        code_challenge = session.get('code_challenge')

        if not session_state or not code_challenge:
            raise E

        if state != session_state:
            raise E

        headers = {'Authorization': f'Basic {settings.SECRETS.TWITTER_AUTH}'}

        params = {
            'grant_type': 'authorization_code',
            'client_id': 'MjRXdnA1WV9PLUVRamM4UUVOamw6MTpjaQ',
            'code': code,
            'code_verifier': code_challenge,
            'redirect_uri': f'{host}api/account/twitter_callback/'
        }

        res = post(ACCESS_TOKEN_URL, params=params, headers=headers)

        if res.status_code != 200:
            raise E

        try:
            res = res.json()
            access_token = res['access_token']
            expires_in = now() + timedelta(seconds=res['expires_in'])
        except:
            raise E

        try:
            twitter = TwitterAccount.objects.get(account=account)
            twitter.access_token = access_token
            twitter.expires_in = expires_in
        except TwitterAccount.DoesNotExist:
            twitter = TwitterAccount(
                account=account,
                access_token=access_token,
                expires_in=expires_in,
            )
        
        try:
            twitter_info(twitter)
        except:
            raise E('Error while processing Twitter Data! Please try again.')

        Thread(target=follow_owners, args=(twitter, )).start()

        return HttpResponseRedirect('/account/')
    except E as e:
        messages.error(request, e.message)
        return HttpResponseRedirect('/')

    except Exception as e:
        logger.exception(e)
        messages.error(request, 'Error to get the Twitter Data')
        return HttpResponseRedirect('/')


@require_GET
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
            'picture_url': data.get('photo_url'),
        }

        account = Account.objects.submit(**submit_data)

        system_login(request, account.user)

        return HttpResponseRedirect('/account/')
    except E as e:
        messages.error(request, e.message)
        return HttpResponseRedirect('/')


@require_GET
def logout(request: HttpRequest):
    system_logout(request)
    return HttpResponseRedirect('/')


@require_GET
@login_required('json')
def get_account(request: HttpRequest):
    try:
        get_token(request)
        user = request.user
        account = request.user.account
        twitter = None

        try:
            ta = account.twitteraccount
            twitter = {
                'user_id': ta.user_id,
                'nickname': ta.nickname,
                'tweets': ta.tweets,
                'username': ta.username,
                'followers': ta.followers,
                'followings': ta.followings,
                'description': ta.description or None,
                'picture': ta._picture,
            }
        except:
            pass

        return JsonResponse({
            'first_name': user.first_name,
            'last_name': user.last_name or None,
            'nickname': account.nickname,
            'wallet': account.wallet,
            'telegram_id': account.telegram_id,
            'username': account.username,
            'picture': account._picture,
            'twitter': twitter,
        })
    except E as e:
        return e.response


@require_POST
@login_required('json')
def update(request: HttpRequest):
    try:
        account = request.user.account
        data = get_data(request)

        try:
            account.twitteraccount
        except TwitterAccount.DoesNotExist:
            raise E('You first need to connect your twitter!')

        try:
            if account.bot_user.total_invites < 3:
                raise
        except:
            raise E('You need to invite 3 PPL in the bot first.')

        wallet = data.get('wallet')

        if not wallet:
            if account.wallet:
                account.wallet = None
                account.save()
            return JsonResponse({
                'ok': 'Your Wallet Successfully Removed',
                'wallet': account.wallet,
            })

        wallet = str(wallet)

        if len(wallet) == 42:
            account.wallet = wallet
            account.save()
            return JsonResponse({
                'ok': 'Your Wallet Successfully Updated',
                'wallet': account.wallet,
            })

        raise E('Invalid Wallet')

    except E as e:
        return e.response


@require_GET
@login_required('json')
def disconnect_twitter(request: HttpRequest):
    try:
        account = request.user.account

        try:
            account.twitteraccount.delete()
        except:
            pass

        return JsonResponse({'ok': 'your twitter was successfully disconnected'})
    except E as e:
        return e.response


@require_GET
def general_info(request: HttpRequest):
    try:
        data = {
            'bot_users': BotUser.objects.count(),
            'accounts': Account.objects.count(),
            'twitters': TwitterAccount.objects.count(),
        }

        return JsonResponse(data)
    except E as e:
        return e.response
