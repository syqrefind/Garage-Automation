# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parking_lot',
            old_name='manager',
            new_name='user',
        ),
    ]