from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from Api.decorators import login_required
from django.views.decorators.http import require_GET


@require_GET
@login_required()
def account(request: HttpRequest):
    user = request.user
    account = user.account

    return HttpResponse(f'{account.username}')