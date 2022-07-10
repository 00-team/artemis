import logging
from base64 import standard_b64decode, standard_b64encode

from django.contrib.auth.models import User
from django.db import IntegrityError, models
from django.db.models import SET_NULL, CharField, PositiveBigIntegerField
from utils.models import hashed_path, username


logger = logging.getLogger(__name__)


class BotUserManager(models.Manager):

    def submit(self, user_id: int, **kwargs):
        lang = kwargs.get('lang')
        if lang:
            lang = str(lang)[:10]

        fullname = kwargs.get('fullname')
        if fullname:
            fullname = str(fullname)[:200].encode()
            fullname = 'base64;' + str(standard_b64encode(fullname), 'utf-8')

        invites_counter = bool(kwargs.get('invites_counter'))
        exists = False

        try:
            bot_user = self.get(user_id=user_id)
            exists = True
            changed = False

            if fullname and bot_user.fullname != fullname:
                bot_user.fullname = fullname
                changed = True

            if lang and bot_user.lang != lang:
                bot_user.lang = lang
                changed = True

            if invites_counter and not bot_user.invites_counter:
                bot_user.invites_counter = True
                changed = True

            try:
                total_invites = int(kwargs['total_invites'])
                if total_invites and bot_user.total_invites != total_invites:
                    bot_user.total_invites = total_invites
                    changed = True

            except:
                pass

            if changed:
                bot_user.save()

        except self.model.DoesNotExist:
            inviter_hash = kwargs.get('inviter')

            bot_user = BotUser(user_id=user_id)

            if fullname:
                bot_user.fullname = fullname

            if lang:
                bot_user.lang = str(lang)[:10]

            if invites_counter:
                bot_user.invites_counter = invites_counter

            try:
                inviter = self.get(invite_hash=inviter_hash)
                bot_user.inviter = inviter
            except:
                pass

            bot_user.save()

        return (bot_user, exists)


class BotUser(models.Model):
    fullname = models.TextField(
        default='None',
        help_text='Encoded User Full Name'
    )
    is_admin = models.BooleanField(default=False)
    user_id = models.BigIntegerField(unique=True)
    lang = CharField(max_length=10, default='en')
    invite_hash = CharField(max_length=128, null=True, blank=True, unique=True)
    total_invites = PositiveBigIntegerField(default=0)
    invites_counter = models.BooleanField(default=False)
    inviter = models.ForeignKey(
        'BotUser',
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )

    objects = BotUserManager()

    @property
    def to_json(self):
        data = {
            'user_id': self.user_id,
            'is_admin': self.is_admin,
            'lang': self.lang,
            'invite_hash': self.invite_hash,
            'total_invites': self.total_invites,
            'invites_counter': self.invites_counter,
            'inviter': None,
            'wallet': None,
        }

        if self.inviter:
            data['inviter'] = {
                'user_id': self.inviter.user_id,
                'invite_hash': self.inviter.invite_hash,
                'total_invites': self.inviter.total_invites,
            }

        try:
            if self.account.wallet:
                data['wallet'] = self.account.wallet
        except:
            pass

        return data

    @property
    def _fullname(self):
        try:
            if self.fullname.startswith('base64;'):
                return str(standard_b64decode(self.fullname[7:]), 'utf-8')

            return self.fullname
        except Exception as e:
            logger.exception(e)
            self.fullname = 'None'
            self.save()

        return self.fullname

    def __str__(self):
        return f'{self._fullname} - {self.user_id}'


class AccountManager(models.Manager):

    def submit(self, telegram_id, **kwargs):
        username = kwargs.get('username') or None
        picture_url = kwargs.get('picture_url') or None

        first_name = kwargs.get('first_name') or ''
        last_name = kwargs.get('last_name') or ''

        first_name = ''.join(filter(lambda c: ord(c) < 128, first_name))
        last_name = ''.join(filter(lambda c: ord(c) < 128, last_name))

        try:
            account = self.get(telegram_id=telegram_id)

            # user
            account.user.first_name = first_name
            account.user.last_name = last_name
            account.user.save()

            # account
            account.username = username
            account.picture_url = picture_url
            account.save()

        except self.model.DoesNotExist:
            user = None

            try:

                user = User(first_name=first_name, last_name=last_name)
                user.save()

                account = Account(
                    user=user,
                    telegram_id=telegram_id,
                    username=username,
                    picture_url=picture_url,
                )
                account.save()

            except IntegrityError:
                if hasattr(user, 'delete'):
                    user.delete()

        return account


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bot_user = models.OneToOneField(
        BotUser, on_delete=SET_NULL,
        null=True, blank=True
    )
    telegram_id = models.BigIntegerField(unique=True)
    username = CharField(max_length=64, blank=True, null=True)
    picture_url = models.URLField(blank=True, null=True)
    picture = models.ImageField(
        upload_to=hashed_path('Account/telegram/picture/', 'telegram_id'),
        blank=True,
        null=True,
    )
    wallet = models.CharField(max_length=42, blank=True, null=True)
    participated = models.BooleanField(default=False)

    objects = AccountManager()

    @property
    def _picture(self) -> str | None:
        if not self.picture:
            return None

        return self.picture.url

    @property
    def nickname(self) -> str:
        nick = self.user.first_name
        if self.user.last_name:
            nick += f' {self.user.last_name}'

        return nick

    def __str__(self):
        return username(self.user)


class TwitterAccount(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    access_token = models.TextField()
    expires_in = models.DateTimeField()

    user_id = CharField(max_length=300, blank=True, null=True)
    nickname = models.TextField(
        default='None', blank=True, null=True,
        help_text='Encoded Nickname'
    )
    username = CharField(max_length=30, blank=True, null=True)
    followers = PositiveBigIntegerField(default=0)
    followings = PositiveBigIntegerField(default=0)
    tweets = PositiveBigIntegerField(default=0)
    description = models.TextField(
        blank=True, null=True,
        help_text='Encoded Description'
    )
    picture_url = models.URLField(blank=True, null=True)
    picture = models.ImageField(
        upload_to=hashed_path('Account/twitter/picture/', 'user_id'),
        blank=True,
        null=True,
    )

    @property
    def _picture(self) -> str | None:
        if not self.picture:
            return None

        return self.picture.url

    @property
    def _nickname(self) -> str:
        try:
            if self.nickname.startswith('base64;'):
                return str(standard_b64decode(self.nickname[7:]), 'utf-8')

            return self.nickname
        except Exception as e:
            logger.exception(e)
            self.nickname = 'None'
            self.save()

        return self.nickname

    @property
    def _description(self) -> str:
        try:
            if self.description.startswith('base64;'):
                return str(standard_b64decode(self.description[7:]), 'utf-8')

            return self.description
        except Exception as e:
            logger.exception(e)
            self.description = ''
            self.save()

        return self.description

    class Meta:
        verbose_name = 'Twitter Account'
        verbose_name_plural = 'Twitter Accounts'

    def __str__(self):
        return username(self.account.user)
