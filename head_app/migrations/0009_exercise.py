# Generated by Django 3.0.4 on 2020-03-24 20:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0008_auto_20200322_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Задание')),
                ('file', models.FileField(blank=True, null=True, upload_to='documents_upload')),
            ],
        ),
    ]
