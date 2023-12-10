from django.contrib import admin

from apps.home.models import Setting, AboutUs, Harassment
from modeltranslation.admin import TranslationAdmin


class SettingAdmin(TranslationAdmin):
    list_display = ['title', 'address_text', 'phone']






admin.site.register(Setting, SettingAdmin)
admin.site.register(Harassment)
admin.site.register(AboutUs)
