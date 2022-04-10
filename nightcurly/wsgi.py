import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('NIGHTCURLY_MODE') == 'DEV':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nightcurly.settings')
else:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'nightcurly.build_settings'
    )

application = get_wsgi_application()
