# Generated by Django 3.0.4 on 2020-08-01 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0027_remove_answervpr_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testvpr_student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testvpr_student',
            name='surname',
        ),
    ]
