# Generated by Django 3.0.4 on 2020-03-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0011_auto_20200326_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='ansex',
            name='ex_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
