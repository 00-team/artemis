from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    return render(request, 'home.html', {})


def error_400(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '400', 'error_text': 'Bad Request'}
    return render(request, 'error.html', context, status=400)


def error_403(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '403', 'error_text': 'Permission Denied'}
    return render(request, 'error.html', context, status=403)


def error_404(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '404', 'error_text': 'Page Not Found'}
    return render(request, 'error.html', context, status=404)


def error_500(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '500', 'error_text': 'Server Error'}
    return render(request, 'error.html', context, status=500)