# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import rest_framework_api_key.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_api_key', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(default=rest_framework_api_key.helpers.generate_key, max_length=40, unique=True),
        ),
    ]
