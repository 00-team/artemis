from django.http import HttpRequest

# shortcuts
from django.shortcuts import render

# decorators
from django.views.decorators.http import require_GET
from django.contrib.admin.views.decorators import staff_member_required

# exceptions
from utils.api import E

# models
from Account.models import Account

# filters
from django.db.models import Q


@require_GET
@staff_member_required
def wallets(request: HttpRequest):
    try:
        def GA(a: Account):
            return str(a.wallet)

        accounts = Account.objects.filter(~Q(wallet=None), participated=False)

        accounts_wallets = list(map(GA, accounts))

        accounts.update(participated=True)

        context = {'wallets': accounts_wallets}

        return render(request, 'wallets.html', context)
    except E as e:
        return e.response
