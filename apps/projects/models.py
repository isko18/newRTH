from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from apps.utils.filesize import file_size
from django.urls import reverse


class Projects(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name="Название проекта")
    project_desc = RichTextUploadingField(blank=True, null=True, verbose_name="Описание баннера №1")
    video = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Видео проекта",
        help_text="сюда нужно поставить ссылку на видео из YouTube. Например: https://www.youtube-nocookie.com/embed/tGTUTXYDhb8?controls=0 "
    )
    image = models.ImageField(
        upload_to="projects/", blank=True, null=True, verbose_name="Фото проекта",
        help_text="сюда загружаем фото в формате JPG или PNG.\n МАКСИМАЛЬНЫЙ РАЗМЕР 1MB(мегабайт), чтобы не заполнять память хостинга",
        validators=[file_size]
    )
    purpose = models.TextField(verbose_name="Описание цели проекта", blank=True, null=True)
    members = models.TextField(verbose_name="Участники проекта", blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"ID: {self.id} -------- название проекта: {self.title}"

    def get_absolute_url(self):
        return reverse("projects_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Проекты"
        verbose_name = "проект"


class InisiativMiniProjects(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name="Название")
    project_desc = RichTextUploadingField(blank=True, null=True, verbose_name="Описание №1")
    video = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Видео проекта",
        help_text="сюда нужно поставить ссылку на видео из YouTube. Например: https://www.youtube-nocookie.com/embed/tGTUTXYDhb8?controls=0 "
    )
    image = models.ImageField(
        upload_to="projects/", blank=True, null=True, verbose_name="Фото проекта",
        help_text="сюда загружаем фото в формате JPG или PNG.\n МАКСИМАЛЬНЫЙ РАЗМЕР 1MB(мегабайт), чтобы не заполнять память хостинга",
        validators=[file_size]
    )
    purpose = models.TextField(verbose_name="Описание цели проекта", blank=True, null=True)
    members = models.TextField(verbose_name="Участники проекта", blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"ID: {self.id} -------- название: {self.title}"

    def get_absolute_url(self):
        return reverse("inisiativ_mini_projects_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Инициативы и Мини проекты"
        verbose_name = "Инициативы и Мини проекты"


class ProjectsPhoto(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True,
                                verbose_name="К какому проекту относится")
    image = models.ImageField(
        upload_to="projects/", verbose_name="Фото проекта",
        help_text="сюда загружаем фото в формате JPG или PNG.\n МАКСИМАЛЬНЫЙ РАЗМЕР 1MB(мегабайт), чтобы не заполнять память хостинга",
        validators=[file_size]
    )

    def __str__(self):
        return f"id: {self.id} -------- проект: {self.project}"

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="80px">'.format(self.image.url))

    image_tag.short_description = 'Фото проекта'

    class Meta:
        verbose_name_plural = "Фото проекта"
        verbose_name = "фото проекта"


class Gallery(models.Model):
    image = models.ImageField(
        upload_to="gallery/", verbose_name="Фото галереи", blank=True, null=True,
        help_text="сюда загружаем фото в формате JPG или PNG.\n МАКСИМАЛЬНЫЙ РАЗМЕР 1MB(мегабайт), чтобы не заполнять память хостинга",
        validators=[file_size]
    )

    def __str__(self):
        return f"ID: {self.id}"

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="80px">'.format(self.image.url))

    image_tag.short_description = 'Фото галереи'

    class Meta:
        verbose_name_plural = "Галерея"
        verbose_name = "галерея"


class Partners(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название партнеров")
    part_desc = models.TextField(verbose_name="Описание партнеров")
    logo = models.ImageField(
        upload_to="partners/", blank=True, null=True,
        help_text="сюда загружаем фото в формате JPG или PNG.\n МАКСИМАЛЬНЫЙ РАЗМЕР 1MB(мегабайт), чтобы не заполнять память хостинга",
        validators=[file_size]
    )
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.logo.url}"

    def image_tag(self):
        if self.logo.url is not None:
            return mark_safe('<img src="{}" height="80px">'.format(self.logo.url))

    image_tag.short_description = 'Лого'

    def get_absolute_url(self):
        return reverse("partners_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Партнёры"
        verbose_name = "партнёр"