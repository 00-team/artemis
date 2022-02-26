from django.contrib import admin

# django utils
from django.utils.html import format_html

# models
from .models import Owner, Asset


def pic(url: str, height: int = 100):
    return format_html(f'<img src={url} height={height} />')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'twitter', 'floor_price', 'ceil_price',
                    'small_pic')
    readonly_fields = ('twitter_id', 'small_pic', 'big_pic')
    save_on_top = True

    fieldsets = (
        ('Main', {
            'fields': (
                'username',
                'picture',
                'twitter',
                'wallet',
                'description',
                'floor_price',
                'ceil_price',
            )
        }),
        ('Details', {
            'fields': ('twitter_id', 'big_pic')
        }),
    )

    @admin.display
    def small_pic(self, owner):
        if not owner.picture:
            return 'None'

        return pic(owner.picture.url)

    @admin.display
    def big_pic(self, owner):
        if not owner.picture:
            return 'None'

        return pic(owner.picture.url, 300)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    readonly_fields = ('img', )
    list_display = ('__str__', 'img')

    @admin.display
    def img(self, asset):
        if not asset.image:
            return 'None'

        return pic(asset.image.url, 150)