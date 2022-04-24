# signals
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver

# models
from Account.models import TwitterAccount

# utils
from utils.models import download_file

# webhooks
from utils.webhook.hooks import twitter_hook

# logger
import logging
logger = logging.getLogger(__name__)


DEL_KWARGS = {'save': False}


# media - profile picture
@receiver(pre_save, sender=TwitterAccount, weak=False)
def twitter_pre_save(sender, instance, **kwargs):
    try:

        if not instance.picture_url:
            instance.picture.delete(**DEL_KWARGS)
            return

        try:
            old_instance = sender.objects.get(id=instance.id)
            old_instance.picture.delete(**DEL_KWARGS)
        except:
            pass

        picture = download_file(instance.picture_url)

        if picture:
            instance.picture = picture

    except Exception as e:
        logger.exception(e)


@receiver(post_save, sender=TwitterAccount, weak=False)
def twitter_post_save(instance, created, **kwargs):
    try:
        status = 'connect' if created else 'reconnect'
        twitter_hook(instance, status)
    except Exception as e:
        logger.exception(e)


@receiver(pre_delete, sender=TwitterAccount, weak=False)
def twitter_pre_delete(instance, **kwargs):
    try:
        instance.picture.delete(**DEL_KWARGS)
        twitter_hook(instance, 'disconnect')
    except Exception as e:
        logger.exception(e)
