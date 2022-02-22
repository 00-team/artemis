from django.http import HttpResponseRedirect

# exceptions
from utils.api import E

# settings
from django.conf import settings


def login_required(response_type: str = 'redirect'):

    def _decorator(view_func):

        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated:
                account = None

                try:
                    account = request.user.account
                except:
                    pass

                if account:
                    return view_func(request, *args, **kwargs)

            if response_type == 'redirect':
                return HttpResponseRedirect(settings.LOGIN_URL)
            else:
                return E('Login Required', 401).response

        return wrap

    return _decorator
