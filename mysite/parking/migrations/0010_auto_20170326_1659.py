# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 20:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0009_auto_20170326_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='spot_number',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('^[1-9]{0,10}$')]),
        ),
    ]
