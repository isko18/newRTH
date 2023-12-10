from modeltranslation.translator import register, TranslationOptions
from apps.educations import models


@register(models.Common)
class CommonTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text',)


@register(models.Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.Introduction)
class IntroductionTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.Survey)
class SurveyTranslationOptions(TranslationOptions):
    fields = ('course', 'title', 'description',)


@register(models.SurveyQuestion)
class SurveyQuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'survey',)


@register(models.SurveyAnswer)
class SurveyAnswerTranslationOptions(TranslationOptions):
    fields = ('answer', 'question',)


@register(models.WorkSheet)
class WorkSheetTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.Gender)
class GenderTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.GenderNorms)
class GenderNormsTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.GenderDiscrimination)
class GenderDiscriminationTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.GenderNormStereotypes)
class GenderNormStereotypesTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.GenderQuality)
class GenderQualityTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.Laws)
class LawsTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.Statistics)
class StatisticsTranslationOptions(TranslationOptions):
    fields = ('course',)


@register(models.EducationVideo)
class EducationVideoTranslationOptions(TranslationOptions):
    fields = ('course', 'title', 'description',)


@register(models.Test)
class TestTranslationOptions(TranslationOptions):
    fields = ('course', 'title',)


@register(models.TestAnswer)
class TestAnswerTranslationOptions(TranslationOptions):
    fields = ('answer', 'test')


@register(models.TestQuestion)
class TestQuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'test')


@register(models.UserAnswer)
class UserAnswerTranslationOptions(TranslationOptions):
    fields = ('question', 'answer', )
