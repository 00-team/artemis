from Collection.models import HitCount
from django.http import HttpRequest


class HitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.model = HitCount.load()

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        if not request.session.get('hit_counted'):
            self.model.hits += 1
            self.model.save()
            request.session['hit_counted'] = True

        return response
