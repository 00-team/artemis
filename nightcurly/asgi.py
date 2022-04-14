import os

from django.core.asgi import get_asgi_application

from .secrets import get_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_settings())

application = get_asgi_application()
