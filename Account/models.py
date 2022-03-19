from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import User

# utils
from utils.models import file_path, username


class AccountManager(models.Manager):

    def submit(self, telegram_id, **kwargs):
        username = kwargs.get('username') or None
        picture_url = kwargs.get('picture_url') or None

        first_name = kwargs.get('first_name') or ''
        last_name = kwargs.get('last_name') or ''

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

            user = User(first_name=first_name, last_name=last_name)
            user.save()

            account = Account(
                user=user,
                telegram_id=telegram_id,
                username=username,
                picture_url=picture_url,
            )
            account.save()

        return account


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.BigIntegerField()
    username = CharField(
        max_length=64,
        blank=True,
        null=True,
        help_text='Optional',
    )
    picture_url = models.URLField(blank=True, null=True)
    picture = models.ImageField(
        upload_to=file_path('Account/telegram/picture/'),
        blank=True,
        null=True,
    )
    wallet = models.CharField(max_length=42, blank=True, null=True)

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
    nickname = CharField(max_length=300, blank=True, null=True)
    username = CharField(max_length=30, blank=True, null=True)
    followers = models.PositiveBigIntegerField(default=0)
    followings = models.PositiveBigIntegerField(default=0)
    tweets = models.PositiveBigIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    picture_url = models.URLField(blank=True, null=True)
    picture = models.ImageField(
        upload_to=file_path('Account/twitter/picture/'),
        blank=True,
        null=True,
    )

    @property
    def _picture(self) -> str | None:
        if not self.picture:
            return None

        return self.picture.url

    class Meta:
        verbose_name = 'Twitter Account'
        verbose_name_plural = 'Twitter Accounts'

    def __str__(self):
        return username(self.account.user)