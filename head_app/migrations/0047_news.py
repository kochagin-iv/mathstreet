# Generated by Django 3.0.4 on 2020-08-19 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0046_statskr_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('date', models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Время добавления')),
                ('groups', models.TextField(blank=True, default=';', null=True, verbose_name='Задано следующим группам')),
            ],
        ),
    ]
