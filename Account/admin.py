from django.contrib import admin

# models
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass