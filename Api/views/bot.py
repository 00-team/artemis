from django.http import HttpRequest, JsonResponse

# decorators
from django.views.decorators.http import require_GET
from Api.decorators import bot_api

# csrf
from django.middleware.csrf import get_token

# utils
from utils.api import get_data

# exceptions
from utils.api import E
from utils.api.exception import ACCOUNT_NOT_FOUND

# models
from Account.models import BotUser, Account, TwitterAccount


@require_GET
@bot_api
def user_status(request: HttpRequest):
    try:
        get_token(request)
        data = get_data(request)

        try:
            user_id = int(data.get('user_id'))
        except:
            raise E

        account = Account.objects.get(telegram_id=user_id)

        try:
            twitter = TwitterAccount.objects.get(account=account).username
        except:
            twitter = None

        return JsonResponse({
            'user_id': account.telegram_id,
            'wallet': account.wallet,
            'twitter': twitter,
        })

    except E as e:
        return e.response

    except Account.DoesNotExist:
        return ACCOUNT_NOT_FOUND.response


@require_GET
@bot_api
def get_bot_user(request: HttpRequest):
    try:
        get_token(request)
        data = get_data(request)

        try:
            submit_data = {
                'user_id': int(data['user_id']),
                'fullname': data.get('fullname'),
                'lang': data.get('lang'),
                'inviter': data.get('inviter'),
                'total_invites': data.get('total_invites'),
                'CFI': data.get('CFI'),
            }
        except:
            raise E('user_id is invalid!')

        bot_user, exists = BotUser.objects.submit(**submit_data)

        return JsonResponse({**bot_user.to_json, 'exists': exists})
    except E as e:
        return e.response
