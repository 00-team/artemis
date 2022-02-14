from django.http import HttpRequest, HttpResponse


def test(request: HttpRequest):
    return HttpResponse('gg')