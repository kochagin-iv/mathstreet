# Generated by Django 3.0.4 on 2020-08-01 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0026_remove_answervpr_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answervpr',
            name='surname',
        ),
    ]
