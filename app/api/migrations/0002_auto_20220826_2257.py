# Generated by Django 3.1 on 2022-08-26 22:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clicklog',
            name='http_referer',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.CharField(max_length=2000, validators=[django.core.validators.URLValidator()]),
        ),
    ]
