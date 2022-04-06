# Generated by Django 3.0.4 on 2020-03-21 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_app', '0002_auto_20200321_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ex_test_VPR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('test_id', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('ans', models.CharField(blank=True, max_length=100, null=True)),
                ('corr_ans', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test6_VPR_st',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('surname', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]