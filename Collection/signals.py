import logging

# signals
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

# models
from .models import Asset, Owner

# conf
from django.conf import settings

# requests
from requests import get


DEL_KWARGS = {'save': False}

logger = logging.getLogger(__name__)


def get_twitter_id(username: str) -> int:
    url = f'https://api.twitter.com/2/users/by/username/{username}'

    headers = {'Authorization': f'Bearer {settings.TWITTER_BEARER}'}

    try:
        res = get(url, headers=headers)
        res = res.json()
        return int(res['data']['id'])
    except Exception as e:
        return None


@receiver(pre_save, sender=Owner, weak=False)
def owner_pre_save(sender, instance, **kwargs):
    try:
        try:
            cowner = sender.objects.get(id=instance.id)
        except:
            cowner = None

        try:
            if cowner.picture != instance.picture:
                cowner.picture.delete(**DEL_KWARGS)
        except:
            pass

        if instance.twitter:
            if not cowner:
                instance.twitter_id = get_twitter_id(instance.twitter)
            elif cowner.twitter != instance.twitter or not instance.twitter_id:
                instance.twitter_id = get_twitter_id(instance.twitter)
        else:
            instance.twitter_id = None

    except:
        pass


@receiver(pre_delete, sender=Owner, weak=False)
def owner_pre_delete(instance, **kwargs):
    try:
        instance.picture.delete(**DEL_KWARGS)
        instance.banner.delete(**DEL_KWARGS)
    except:
        pass


@receiver(pre_delete, sender=Asset, weak=False)
def assets_pre_delete(instance, **kwargs):
    try:
        instance.image.delete(**DEL_KWARGS)
    except:
        pass
