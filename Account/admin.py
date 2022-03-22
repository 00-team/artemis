from django.contrib import admin

# models
from .models import BotUser
from .models import Account
from .models import TwitterAccount


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(TwitterAccount)
class TwitterAccountAdmin(admin.ModelAdmin):
    readonly_fields = ('account', 'access_token', 'expires_in')
