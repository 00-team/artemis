from django.http import HttpResponseRedirect

# settings
from django.conf import settings


def login_required(view_func):

    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            account = None

            try:
                account = request.user.account
            except:
                pass

            if account:
                return view_func(request, *args, **kwargs)

        return HttpResponseRedirect(settings.LOGIN_URL)

    return wrap
