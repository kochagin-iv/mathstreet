# Generated by Django 3.0.4 on 2020-08-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0033_testvpr_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='testvpr',
            name='is_visible',
            field=models.BooleanField(default=0),
        ),
    ]