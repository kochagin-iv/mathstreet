# Generated by Django 3.0.4 on 2020-04-19 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0021_ansexkr_kr_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ansexkr',
            old_name='description',
            new_name='ans',
        ),
    ]
