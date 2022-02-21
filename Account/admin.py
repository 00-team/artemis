from django.contrib import admin

# models
from .models import Account, TwitterAccount


@admin.register(Account, TwitterAccount)
class AccountAdmin(admin.ModelAdmin):
    pass