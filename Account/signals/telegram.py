# signals
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

# models
from Account.models import Account, BotUser

# utils
from utils.models import download_file
from utils.api import s1

# webhooks
from utils.webhook.hooks import account_hook, bot_user_hook

DEL_KWARGS = {'save': False}


# media - profile picture
@receiver(pre_save, sender=Account)
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

        status = 'new'

        try:
            old_instance = sender.objects.get(id=instance.id)
            status = 'update'
            old_instance.picture.delete(**DEL_KWARGS)
        except:
            pass

        picture, *_ = download_file(instance.picture_url)

        if picture:
            instance.picture = picture

        account_hook(instance, status)
    except:
        pass


@receiver(pre_delete, sender=Account, weak=False)
def account_pre_delete(instance, **kwargs):
    try:
        instance.picture.delete(**DEL_KWARGS)
        account_hook(instance, 'delete')
    except:
        pass


@receiver(pre_save, sender=BotUser, weak=False)
def bot_user_pre_save(instance, **kwargs):
    try:
        if not instance.invite_hash:
            instance.invite_hash = s1(instance.user_id)

        if instance.inviter == instance:
            instance.inviter = None

        if not instance.inviter:
            instance.CFI = False

        bot_user_hook(instance)
    except:
        pass
