from django.contrib import admin

from apps.educations import models
from modeltranslation.admin import TranslationAdmin


class ImageTabularAdmin(admin.TabularInline):
    model = models.StatisticImages
    extra = 3


class SurveyQuestionTabularAdmin(admin.TabularInline):
    model = models.SurveyQuestion
    extra = 3
    fk_name = 'survey'


class SurveyAnswerTabularAdmin(admin.TabularInline):
    model = models.SurveyAnswer
    extra = 3
    fk_name = 'question'


class TestQuestionTabularAdmin(admin.TabularInline):
    model = models.TestQuestion
    extra = 3


class TestAnswerTabularAdmin(admin.TabularInline):
    model = models.TestAnswer
    extra = 3
    fk_name = 'test'


class CommonAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


class SurveyAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    inlines = [SurveyQuestionTabularAdmin]


class SurveyQuestionAdmin(TranslationAdmin):
    list_display = ('question',)
    search_fields = ('question',)
    inlines = [SurveyAnswerTabularAdmin]


class StatisticsAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    inlines = [ImageTabularAdmin]


class TestAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    inlines = [TestQuestionTabularAdmin, ]


class TestQuestionAdmin(TranslationAdmin):
    list_display = ('question',)
    search_fields = ('question',)
    inlines = [TestAnswerTabularAdmin]


admin.site.register(models.Introduction, CommonAdmin)
admin.site.register(models.Survey, SurveyAdmin)
admin.site.register(models.Statistics, StatisticsAdmin)
admin.site.register(models.SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(models.WorkSheet, CommonAdmin)
admin.site.register(models.Gender, CommonAdmin)
admin.site.register(models.GenderQuality, CommonAdmin)
admin.site.register(models.GenderDiscrimination, CommonAdmin)
admin.site.register(models.GenderNorms, CommonAdmin)
admin.site.register(models.GenderNormStereotypes, CommonAdmin)
admin.site.register(models.Laws, CommonAdmin)
admin.site.register(models.Test, TestAdmin)
admin.site.register(models.TestQuestion, TestQuestionAdmin)
admin.site.register(models.EducationVideo, CommonAdmin)
admin.site.register(models.Courses)
