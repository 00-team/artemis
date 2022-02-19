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

# models
from Account.models import Account
from utils.api.exception import ACCOUNT_NOT_FOUND


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

        return JsonResponse({
            'user_id': account.telegram_id,
            'wallet': account.wallet,
        })

    except E as e:
        return e.response

    except Account.DoesNotExist:
        return ACCOUNT_NOT_FOUND.response