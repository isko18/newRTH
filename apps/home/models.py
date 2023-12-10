from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Setting(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название сайта")
    icon = models.ImageField(blank=True,upload_to='images/', verbose_name="Логотип")
    keywords = models.TextField(max_length=255, blank=True, null=True, verbose_name="Ключевые слова для поиска")
    description = models.TextField(blank=True,null=True, verbose_name="Пара слов для поиска")
    address_text = models.CharField(blank=True,max_length=255, null=True, verbose_name="Адрес")
    address_link = models.CharField(blank=True,max_length=255, null=True, verbose_name="Ссылка на расположение по карте")
    phone = models.CharField(blank=True,max_length=25, null=True, verbose_name="Телефон")
    email = models.CharField(blank=True,max_length=250, null=True, verbose_name="Электронная почта")

    whatsapp = models.CharField(
        blank=True,max_length=255, null=True,
        help_text="Поставьте сюда ссылку на whatsapp, например: https://wa.me/+996700400400")
    telegram = models.CharField(
        blank=True,max_length=255, null=True,
        help_text="Поставьте сюда ссылку на telegram, например: https://t.me/noviritm")
    facebook = models.CharField(
        blank=True,max_length=255, null=True,
        help_text="Поставьте сюда ссылку на facebook, например: https://www.facebook.com/newrhythm")
    instagram = models.CharField(
        blank=True,max_length=255, null=True,
        help_text="Поставьте сюда ссылку на instagram, например: https://www.instagram.com/noviritm/")
    twitter = models.CharField(
        blank=True,max_length=255, null=True,
        help_text="Поставьте сюда ссылку на twitter, например: https://twitter.com/NoviRitm_2014")
    youtube = models.CharField(
        blank=True, max_length=255, null=True,
        help_text="Поставьте сюда ссылку на youtube, например: https://www.youtube.com/channel/UC5YyBkynZRxAIKSGBzMlftw")

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Основные настройки"
        verbose_name = "основные настройки"


class AboutUs(models.Model):
    banner_title_1 = models.CharField(blank=True, max_length=233, null=True, verbose_name="Заголовок баннера №1")
    banner_desc_1 = RichTextUploadingField(blank=True, null=True, verbose_name="Описание баннера №1")
    aboutus_title_1 = RichTextUploadingField(blank=True, null=True, verbose_name="Блок №1")
    aboutus_title_2 = RichTextUploadingField(blank=True, null=True, verbose_name="Блок №2")
    aboutus_title_3 = RichTextUploadingField(blank=True, null=True, verbose_name="Блок №3")

    def __str__(self):
        return f"ID: {str(self.id)} / Блок о нас"

    class Meta:
        verbose_name_plural = "О нас - главная стр"
        verbose_name = "О нас - главная стр"


class Harassment(models.Model):
    banner_title_1 = models.CharField(
        blank=True, max_length=233, null=True, verbose_name="название"
    )
    harassment_desc = RichTextUploadingField(
        blank=True, null=True, verbose_name="Описание харассмента"
    )

    def __str__(self):
        return f"ID: {str(self.id)} / Обучение стр"

    class Meta:
        verbose_name_plural = "харассмент - обучение стр"
        verbose_name = "харассмент - обучение стр"