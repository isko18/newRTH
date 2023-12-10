from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Common(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255, null=True, blank=True
    )
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True
    )
    text = models.TextField(
        verbose_name='Текст', null=True, blank=True
    )

    class Meta:
        abstract = True


class Courses(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название oбучение',
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Обучение'
        verbose_name_plural = 'Обучение'
        ordering = ('-id',)


class Introduction(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_intro'
    )
    image = models.ImageField(
        verbose_name='Изображение', upload_to='introduction_image/',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Введение'
        verbose_name_plural = 'Введение'

    def __str__(self):
        return self.title


class Survey(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_servey'
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=255, null=True, blank=True
    )
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опрос'

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    question = models.TextField(
        verbose_name='Вопрос Опроса',
        null=True, blank=True
    )
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name='survey_question'
    )

    class Meta:
        verbose_name = 'Вопрос Опроса'
        verbose_name_plural = 'Вопросы Опроса'


class SurveyAnswer(models.Model):
    answer = models.TextField(
        verbose_name='Ответ Опроса',
        null=True, blank=True
    )
    question = models.ForeignKey(
        SurveyQuestion, on_delete=models.CASCADE, related_name='survey_answer'
    )

    class Meta:
        verbose_name = 'Ответ Опроса'
        verbose_name_plural = 'Ответы Опроса'


class WorkSheet(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_worksheet'
    )
    file = models.FileField(
        verbose_name='Рабочая Тетрадь',
        upload_to='worksheet_pdf',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Рабочая Тетрадь'
        verbose_name_plural = 'Рабочии Тетради'

    def __str__(self):
        return self.title


class Gender(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_gender'
    )

    class Meta:
        verbose_name = 'Гендер и Пол'
        verbose_name_plural = 'Гендер и Пол'

    def __str__(self):
        return self.title


class GenderDiscrimination(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_gender_discrim'
    )

    class Meta:
        verbose_name = 'Гендерная Дискриминация'
        verbose_name_plural = 'Гендерная Дискриминация'

    def __str__(self):
        return self.title


class GenderNorms(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_gender_norms'
    )

    class Meta:
        verbose_name = 'Гендерные Нормы'
        verbose_name_plural = 'Гендерные Нормы'

    def __str__(self):
        return self.title


class GenderNormStereotypes(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_gender_norm'
    )

    class Meta:
        verbose_name = 'Гендерные Стериотипы'
        verbose_name_plural = 'Гендерные Стериотипы'

    def __str__(self):
        return self.title


class GenderQuality(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_gender_quality',
    )

    class Meta:
        verbose_name = 'Способы Продвижения Гендерного Равенства'
        verbose_name_plural = 'Способы Продвижения Гендерного Равенства'

    def __str__(self):
        return self.title


class Laws(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_laws'
    )

    class Meta:
        verbose_name = 'Законы КР о Гендерной Политике'
        verbose_name_plural = 'Законы КР о Гендерной Политике'

    def __str__(self):
        return self.title


class Statistics(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_statistics'
    )

    class Meta:
        verbose_name = 'Статистика ЦА'
        verbose_name_plural = 'Статистика ЦА'

    def __str__(self):
        return self.title


class StatisticImages(models.Model):
    statistic_page = models.ForeignKey(
        Statistics, on_delete=models.CASCADE, related_name='statistic_image'
    )
    image = models.ImageField(
        verbose_name='Изображение Статистики', upload_to='statistic_image/',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Изображение Статистики'
        verbose_name_plural = 'Изображения Статстики'


class EducationVideo(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_edus'
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=255, null=True, blank=True
    )
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True
    )
    video = models.FileField(
        verbose_name='Видео с обучениями', upload_to='video_education/',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Видео с Обучениями'
        verbose_name_plural = 'Видео с Обучениями'

    def __str__(self):
        return self.title


class Test(Common):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='course_test'
    )
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
    )

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title


class TestQuestion(models.Model):
    question = models.TextField(
        verbose_name='Вопрос Теста',
        null=True, blank=True
    )
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name='test_question'
    )

    class Meta:
        verbose_name = 'Вопрос Теста'
        verbose_name_plural = 'Вопросы Теста'


class TestAnswer(models.Model):
    answer = models.TextField(
        verbose_name='Ответ Теста',
        null=True, blank=True
    )
    test = models.ForeignKey(
        TestQuestion, on_delete=models.CASCADE, related_name='test_answer'
    )

    class Meta:
        verbose_name = 'Ответ Теста'
        verbose_name_plural = 'Ответы Теста'


class UserAnswer(models.Model):
    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_answer'
    )

