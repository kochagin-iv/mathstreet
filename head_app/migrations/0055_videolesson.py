# Generated by Django 3.0.4 on 2021-04-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0054_auto_20200828_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200, verbose_name='Ссылка на видео')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название видео')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Описание под видео')),
            ],
        ),
    ]
