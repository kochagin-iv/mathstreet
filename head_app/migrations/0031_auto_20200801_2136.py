# Generated by Django 3.0.4 on 2020-08-01 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0030_auto_20200801_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ansex',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='ansex',
            name='surname',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]
