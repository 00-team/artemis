from django.http import HttpRequest, Http404
from django.shortcuts import render

from .models import Owner


def owners(request: HttpRequest, username):
    exists = Owner.objects.filter(username=username).exists()

    if not exists:
        raise Http404('Owner not found')

    return render(request, 'owners.html', {'owner': username})
