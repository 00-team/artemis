# signals
from django.db.models.signals import pre_save
from django.dispatch import receiver

# utils
from django.utils.crypto import get_random_string

# models
from django.contrib.auth.models import User


# random username
@receiver(pre_save, sender=User)
def user_pre_save(instance, **kwargs):
    if not instance.username:
        while True:
            username = get_random_string(32)
            if User.objects.filter(username=username).exists():
                continue
            else:
                instance.username = username
                break