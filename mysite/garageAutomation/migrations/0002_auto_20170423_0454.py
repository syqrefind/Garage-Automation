# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garageAutomation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='account',
        ),
        migrations.AddField(
            model_name='account',
            name='paymentmethods',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='garageAutomation.PaymentMethod'),
            preserve_default=False,
        ),
    ]
