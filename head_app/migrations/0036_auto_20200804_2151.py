# Generated by Django 3.0.4 on 2020-08-04 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0035_kr_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kr',
            name='visible',
            field=models.BooleanField(blank=True, default=0, verbose_name='Работа видна'),
        ),
    ]
