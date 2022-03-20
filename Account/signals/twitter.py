# signals
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

# models
from Account.models import TwitterAccount

# threading
from threading import Thread

# utils
from utils.models import download_file

# webhooks
from utils.webhook.hooks import twitter_hook

DEL_KWARGS = {'save': False}


def twitter_profile(instance, status):
    try:
        picture = download_file(instance.picture_url)

        if picture:
            instance.picture.save('picture.jpg', picture)

        twitter_hook(instance, status)
    except:
        pass


# media - profile picture
@receiver(pre_save, sender=TwitterAccount)
def twitter_pre_save(sender, instance, **kwargs):
    try:
        try:
            old_instance = sender.objects.get(id=instance.id)
        except:
            old_instance = None

        try:
            if old_instance.picture != instance.picture:
                old_instance.picture.delete(**DEL_KWARGS)
        except:
            pass

        try:
            status = 'reconnect' if old_instance else 'connect'
            if not instance.picture_url:
                twitter_hook(instance, status)
                return

            if old_instance:
                if old_instance.picture_url == instance.picture_url and instance.picture:
                    if old_instance.picture:
                        twitter_hook(instance, status)
                    return

            thread = Thread(target=twitter_profile, args=(instance, status))
            thread.start()

        except:
            pass

    except:
        pass


@receiver(pre_delete, sender=TwitterAccount)
def twitter_pre_delete(instance, **kwargs):
    try:
        instance.picture.delete(**DEL_KWARGS)
        twitter_hook(instance, 'disconnect')
    except:
        pass
