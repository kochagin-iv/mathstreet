# Generated by Django 3.0.4 on 2020-03-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0007_answervpr_is_corr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answervpr',
            name='ans',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
