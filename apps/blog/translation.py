from modeltranslation.translator import register, TranslationOptions
from apps.blog.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'slug')
