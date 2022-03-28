from django.contrib import admin

from django.utils.html import format_html

# models
from .models import BotUser
from .models import Account
from .models import TwitterAccount


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'user_id', 'fullname',
        'lang', 'total_invites', 'is_admin',
    )
    readonly_fields = ('user_id', 'lang', 'invite_hash', 'has_logedin')
    list_filter = ('is_admin', 'lang')
    search_fields = ('user_id', 'invite_hash')

    fieldsets = (
        ('Data', {'fields': ('fullname', 'is_admin')}),
        ('Invites', {'fields': ('total_invites', 'CFI', 'inviter')}),
        ('Details', {
            'fields': ('user_id', 'invite_hash', 'lang', 'has_logedin')
        }),
    )

    @admin.display
    def has_logedin(self, obj):
        try:
            url = f'/admin/Account/account/{obj.account.id}/change/'
            return format_html(f'<a href="{url}">{obj.account}</a>')
        except:
            return 'No'


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'telegram_id', 'username', 'pic')
    readonly_fields = ('pic', )
    search_fields = ('username', 'telegram_id')

    @admin.display
    def pic(self, obj):
        if obj._picture:
            return format_html((
                f'<img src="{obj._picture}" '
                'height="121" style="border-radius:7px" />'
            ))

        return 'None'


@admin.register(TwitterAccount)
class TwitterAccountAdmin(admin.ModelAdmin):
    readonly_fields = ('account', 'access_token', 'expires_in')
