import os

from django.core.wsgi import get_wsgi_application

from .secrets import get_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_settings())

application = get_wsgi_application()
