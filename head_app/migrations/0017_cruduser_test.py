# Generated by Django 3.0.4 on 2020-04-13 15:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0016_cruduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruduser',
            name='test',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Задание'),
        ),
    ]
