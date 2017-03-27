# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 22:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0007_auto_20170324_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='amount_charged',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='session',
            name='license_plate_number',
            field=models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator('^[A-Z0-9]{6,7}$')]),
        ),
        migrations.AlterField(
            model_name='session',
            name='stay_length',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='session',
            name='time_arrived',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='session',
            name='time_exited',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]