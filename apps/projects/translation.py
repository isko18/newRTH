from modeltranslation.translator import register, TranslationOptions
from apps.projects.models import Projects, InisiativMiniProjects, Partners


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'project_desc', 'purpose', 'members')


@register(InisiativMiniProjects)
class InisiativMiniProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'project_desc', 'purpose', 'members')


@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'part_desc',)
