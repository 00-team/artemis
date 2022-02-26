from django.test import TestCase

from django.core.files import File
from django.conf import settings

from .models import Owner

owner_picture = File(open(settings.BASE_DIR / 'static/img/00-Team.png', 'rb'))
master_wallet = '0x7aE0A149Ce992145078b6E44091fec5358E7AE9A'


class OwnerTestCase(TestCase):

    def setUp(self):
        Owner.objects.create(
            username='Master',
            picture=owner_picture,
            wallet=master_wallet,
            description='Master is Grate',
            floor_price='0.1',
            ceil_price='1',
        )

    def test_owners(self):
        '''Owners Test'''
        master = Owner.objects.get(username='Master')
        self.assertEqual(master.wallet, master_wallet)
        master.delete()
