# Generated by Django 3.0.4 on 2020-03-21 14:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]