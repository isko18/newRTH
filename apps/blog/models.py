from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок новостей")
    img = models.ImageField(verbose_name="Фото картинок")
    description = RichTextUploadingField(blank=True, null=True, verbose_name="Описание новостей")
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "новость"

    def __str__(self):
        return self.title
