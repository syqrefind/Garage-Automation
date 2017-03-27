# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0010_remove_registereduser_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestuser',
            name='CC',
        ),
        migrations.AlterField(
            model_name='session',
            name='time_arrived',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='session',
            name='time_exited',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]