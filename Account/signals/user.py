from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string


# random username
@receiver(pre_save, sender=User, weak=False)
def user_pre_save(instance, **kwargs):
    if not instance.username:
        while True:
            username = 'RU-' + get_random_string(32)
            if User.objects.filter(username=username).exists():
                continue
            else:
                instance.username = username
                break
