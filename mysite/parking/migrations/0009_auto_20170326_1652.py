# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 20:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0008_auto_20170324_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='spot_number',
            field=models.IntegerField(max_length=10, validators=[django.core.validators.RegexValidator('^[1-9]{0,10}$')]),
        ),
    ]
