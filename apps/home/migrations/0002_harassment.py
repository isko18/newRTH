# Generated by Django 4.0.3 on 2022-03-17 13:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harassment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title_1', models.CharField(blank=True, max_length=233, null=True, verbose_name='название')),
                ('harassment_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание харассмента')),
            ],
            options={
                'verbose_name': 'харассмент - обучение стр',
                'verbose_name_plural': 'харассмент - обучение стр',
            },
        ),
    ]
