# Generated by Django 3.0.4 on 2020-04-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0015_testvpr_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrudUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
