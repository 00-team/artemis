import os

from django.core.asgi import get_asgi_application

if os.environ.get('NIGHTCURLY_MODE') == 'DEV':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nightcurly.settings')
else:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'nightcurly.build_settings'
    )

application = get_asgi_application()
