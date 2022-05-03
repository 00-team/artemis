from Collection.models import HitCount
from django.http import HttpRequest


DISALLOWED_PATHS = ('/api', '/favicon.ico', '/admin', '/robots.txt')


class HitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)

        if request.path.startswith(DISALLOWED_PATHS):
            return response

        if not request.session.get('hit_counted'):
            hit_count = HitCount.load()
            hit_count.hits += 1
            hit_count.save()
            request.session['hit_counted'] = True

        return response
