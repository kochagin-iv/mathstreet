# Generated by Django 3.0.4 on 2020-04-17 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0019_ansexkr_exkr'),
    ]

    operations = [
        migrations.CreateModel(
            name='KrSt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('kr_id', models.IntegerField(verbose_name='ключ связи с кр')),
            ],
        ),
    ]
