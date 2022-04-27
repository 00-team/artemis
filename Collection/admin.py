from django.contrib import admin
# django utils
from django.utils.html import format_html

# models
from .models import FAQ, Asset, HitCount, Owner


def pic(url: str, height: int = 100):
    return format_html(f'<img src={url} height={height} />')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'twitter', 'floor_price', 'ceil_price',
                    'small_pic')
    readonly_fields = ('twitter_id', 'small_pic', 'big_pic', '_banner')
    save_on_top = True

    fieldsets = (
        ('Main', {
            'fields': (
                'username',
                'rarible',
                'instagram',
                'wallet',
                'description',
                'floor_price',
                'ceil_price',
            )
        }),
        ('Photos', {
            'fields': ('picture', 'banner')
        }),
        ('Twitter', {
            'fields': ('twitter', 'tweet')
        }),
        ('Details', {
            'fields': ('twitter_id', 'big_pic', '_banner')
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

    @admin.display
    def _banner(self, owner):
        if not owner.banner:
            return 'None'

        return pic(owner.banner.url, 400)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    readonly_fields = ('img', )
    list_display = ('__str__', 'img')

    @admin.display
    def img(self, asset):
        if not asset.image:
            return 'None'

        return pic(asset.image.url, 150)


@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'owner')


@admin.register(HitCount)
class HitCountAdmin(admin.ModelAdmin):

    def get_actions(self, *args, **kwargs):
        return []

    def change_view(self, request, object_id, form_url='', extra_context={}):
        extra_context['show_save_and_add_another'] = False
        return super().change_view(request, object_id, form_url, extra_context)
