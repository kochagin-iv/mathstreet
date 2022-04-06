# Generated by Django 3.0.4 on 2020-08-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0047_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='short_text',
            field=models.TextField(blank=True, verbose_name='Короткий заголовок(при необходимости)'),
        ),
        migrations.AddField(
            model_name='news',
            name='visible_for_all',
            field=models.BooleanField(default=False, verbose_name='Новость видна всем'),
        ),
    ]