# Generated by Django 3.0.4 on 2020-08-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0032_auto_20200801_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='testvpr',
            name='groups',
            field=models.TextField(blank=True, default=';', null=True, verbose_name='Задано следующим группам'),
        ),
    ]
