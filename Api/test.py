import hmac
from hashlib import sha256

from django.conf import settings
from django.test import Client, TestCase
from django.utils.timezone import now


c = Client()
PHOTO_URL = 'https://cdn.discordapp.com/attachments/731174051170746500/836494236941680650/cock.png'


class AccountTestCase(TestCase):
    base_url = '/api/account/'

    def test_telegram_callback(self):
        now_date = int(now().timestamp())

        data = {
            'id': 7,
            'first_name': 'master',
            'username': 'Master67',
            'auth_date': now_date,
            'photo_url': PHOTO_URL
        }

        data_list = list(map(lambda i: f'{i[0]}={i[1]}', data.items()))
        data_list.sort()

        data_message = '\n'.join(data_list).encode()

        token = sha256(settings.SECRETS.BOT_TOKEN.encode()).digest()

        hashed = hmac.new(token, msg=data_message, digestmod=sha256)
        hashed = hashed.hexdigest()

        data['hash'] = hashed

        response = c.get(
            self.base_url + 'telegram_callback/',
            follow=True,
            data=data,
        )

        self.assertEqual(response.wsgi_request.path, '/account/')

        response = c.get(
            self.base_url + 'telegram_callback/',
            follow=True,
        )

        self.assertEqual(response.wsgi_request.path, '/')
