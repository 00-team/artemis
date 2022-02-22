from django.contrib import admin

# models
from .models import Account, TwitterAccount


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(TwitterAccount)
class TwitterAccountAdmin(admin.ModelAdmin):
    readonly_fields = ('account', 'access_token', 'expires_in')