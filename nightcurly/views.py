from django.http import HttpRequest
from django.shortcuts import render


def home(request: HttpRequest):
    return render(request, 'home.html', {})


def error_400(request: HttpRequest, exception=None, **kwargs):
    context = {'error': {
        'code': '400',
        'title': 'Bad Request',
        'description': 'Bad Request description ...'
    }}
    return render(request, 'error.html', context, status=400)


def error_403(request: HttpRequest, exception=None, **kwargs):
    context = {'error': {
        'code': '403',
        'title': 'Permission Denied',
        'description': 'description ...'
    }}
    return render(request, 'error.html', context, status=403)


def error_404(request: HttpRequest, exception=None, **kwargs):
    context = {'error': {
        'code': '404',
        'title': 'Page Not Found',
        'description': ':('
    }}
    return render(request, 'error.html', context, status=404)


def error_500(request: HttpRequest, exception=None, **kwargs):
    context = {'error': {
        'code': '500',
        'title': 'Server Error',
        'description': 'Server Error description'
    }}
    return render(request, 'error.html', context, status=500)
