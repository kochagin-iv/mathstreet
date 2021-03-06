# Generated by Django 3.0.4 on 2020-08-20 12:41

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0048_auto_20200820_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='file',
            field=models.FileField(blank=True, upload_to='news_upload/', verbose_name='Файл, прикрепленный к новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
