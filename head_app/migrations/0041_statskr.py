# Generated by Django 3.0.4 on 2020-08-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0040_ansexkr_number_ans'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatsKr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('us_id', models.IntegerField(blank=True, default=-1, verbose_name='ID ученика')),
                ('us_num', models.IntegerField(blank=True, default=1, verbose_name='Номер попытки')),
                ('kr_id', models.IntegerField(verbose_name='ID работы')),
                ('kol_num', models.IntegerField(blank=True, verbose_name='Число заданий в работе')),
                ('kol_corr', models.IntegerField(blank=True, verbose_name='Количество правильных ответов')),
                ('anss', models.TextField(blank=True, verbose_name='Правильно/нет ответил ученик')),
                ('time', models.IntegerField(blank=True, verbose_name='Потраченное время на работу')),
            ],
        ),
    ]