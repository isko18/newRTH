from modeltranslation.translator import register, TranslationOptions
from apps.home.models import AboutUs, Harassment, Setting


@register(Setting)
class SettingTranslationOptions(TranslationOptions):
    fields = ('title', 'keywords', 'description',)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('banner_title_1', 'banner_desc_1', 'aboutus_title_1', 'aboutus_title_2', 'aboutus_title_3')


@register(Harassment)
class HarassmentTranslationOptions(TranslationOptions):
    fields = ('banner_title_1', 'harassment_desc')
