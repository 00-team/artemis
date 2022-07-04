import logging

from Account.models import Account, BotUser
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from utils.api import s1
from utils.models import download_file
from utils.models.file import get_ext, get_hased_item
from utils.webhook.hooks import account_hook, bot_user_hook


logger = logging.getLogger(__name__)


DEL_KWARGS = {'save': False}


# media - profile picture
@receiver(pre_save, sender=Account, weak=False)
def account_pre_save(sender, instance, **kwargs):
    try:
        try:
            instance.bot_user = BotUser.objects.get(
                user_id=instance.telegram_id
            )
        except:
            instance.bot_user = None

        if not instance.picture_url:
            instance.picture.delete(**DEL_KWARGS)
            return

        try:
            old_instance = sender.objects.get(id=instance.id)
            old_instance.picture.delete(**DEL_KWARGS)
        except:
            pass

    except Exception as e:
        logger.exception(e)


@receiver(post_save, sender=Account, weak=False)
def account_post_save(instance, created, update_fields, **kwargs):
    try:
        if update_fields != None:
            return

        pic = None

        if instance.picture_url:
            hashed = get_hased_item(instance.telegram_id)
            ext = get_ext(instance.picture_url)
            pic = f'/m/Account/telegram/picture/{hashed}.{ext}'

        status = 'new' if created else 'update'
        account_hook(instance, status, picture=pic)

        picture = download_file(instance.picture_url)

        if picture:
            instance.picture = picture
            instance.save(update_fields=['picture'])
            return

    except Exception as e:
        logger.exception(e)


@receiver(pre_delete, sender=Account, weak=False)
def account_pre_delete(instance, **kwargs):
    try:
        instance.picture.delete(**DEL_KWARGS)
        account_hook(instance, 'delete')
    except Exception as e:
        logger.exception(e)


@receiver(pre_save, sender=BotUser)
def bot_user_pre_save(instance, **kwargs):
    try:
        if not instance.invite_hash:
            instance.invite_hash = s1(instance.user_id)

        if instance.inviter == instance:
            instance.inviter = None

        if not instance.inviter:
            instance.invites_counter = False

        bot_user_hook(instance)
    except Exception as e:
        logger.exception(e)
