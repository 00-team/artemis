from django.http import HttpRequest
from django.shortcuts import render


def error_400(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '400', 'error_text': 'Bad Request'}
    return render(request, 'error.html', context)


def error_403(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '403', 'error_text': 'Permission Denied'}
    return render(request, 'error.html', context)


def error_404(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '404', 'error_text': 'Page Not Found'}
    return render(request, 'error.html', context)


def error_500(request: HttpRequest, exception=None, **kwargs):
    context = {'error_code': '500', 'error_text': 'Server Error'}
    return render(request, 'error.html', context)