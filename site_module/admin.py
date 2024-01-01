from django.contrib import admin

from site_module import models


# Register your models here.

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['url', 'is_active']


class BannerAdmin(admin.ModelAdmin):
    fields = ['title', 'url', 'position', 'image', 'is_active']


admin.site.register(models.SiteSetting)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.FooterLink, FooterLinkAdmin)
admin.site.register(models.Slider, SliderAdmin)
admin.site.register(models.SiteBanner, BannerAdmin)
