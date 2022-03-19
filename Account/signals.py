import logging

# signals
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

# models
from .models import Account, TwitterAccount
from django.contrib.auth.models import User

# threading
from threading import Thread

# requests
from requests import get

# webhooks
from utils.webhook.hooks import account_hook

# files
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

DEL_KWARGS = {'save': False}

logger = logging.getLogger(__name__)


def download_picture(instance: Account | TwitterAccount):
    try:
        temp = NamedTemporaryFile()
        with get(instance.picture_url, allow_redirects=True) as res:

            if res.status_code != 200:
                return

            for chunk in res.iter_content(8192):  # 1024 * 8
                temp.write(chunk)

        instance.picture.save('picture.jpg', File(temp))
        instance.save()
    except Exception as e:
        logger.error(e)


# images
@receiver(pre_save, sender=TwitterAccount)
@receiver(pre_save, sender=Account)
def account_pre_save(sender, instance, **kwargs):
    try:
        current_account = sender.objects.get(id=instance.id)

        try:
            if current_account.picture != instance.picture:
                current_account.picture.delete(**DEL_KWARGS)
        except:
            pass

        if current_account.picture_url != instance.picture_url or not instance.picture:
            if not instance.picture_url:
                instance.picture.delete(**DEL_KWARGS)
            else:
                thread = Thread(target=download_picture, args=(instance, ))
                thread.start()

    except:
        pass


@receiver(pre_delete, sender=TwitterAccount)
@receiver(pre_delete, sender=Account)
def account_pre_delete(instance, **kwargs):
    try:
        instance.picture.delete(**DEL_KWARGS)
    except:
        pass


# random username
@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    if not instance.username:
        while True:
            username = get_random_string(32)
            if User.objects.filter(username=username).exists():
                continue
            else:
                instance.username = username
                break


# webhooks
@receiver(post_save, sender=Account)
def webhook_account(instance, created, **kwargs):
    try:
        if created:
            account_hook(instance, 'new')
        else:
            account_hook(instance, 'update')
    except:
        pass