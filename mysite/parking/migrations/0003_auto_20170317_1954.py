# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 23:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20170317_0234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='lot',
            new_name='parkingLot',
        ),
    ]
