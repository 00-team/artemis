from django.contrib import admin

# django utils
from django.utils.html import format_html

# models
from .models import Owner


def pic(url: str, height: int = 100):
    return format_html(f'<img src={url} height={height} />')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'twitter', 'floor_price', 'ceil_price',
                    'small_pic')
    readonly_fields = ('twitter_id', 'small_pic', 'big_pic')

    @admin.display
    def small_pic(self, owner):
        if not owner.picture:
            return 'None'

        return pic(owner.picture.ur)

    @admin.display
    def big_pic(self, owner):
        if not owner.picture:
            return 'None'

        return pic(owner.picture.ur, 500)
