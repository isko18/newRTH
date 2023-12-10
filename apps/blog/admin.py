from django.contrib import admin
from apps.blog.models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')


# admin.site.register(News)
