# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 18:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Credit_Card', models.CharField(blank=True, max_length=16)),
                ('license_plate_number', models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator('^[A-Z0-9]{6,7}$')])),
                ('time_arrived', models.CharField(blank=True, max_length=10)),
                ('time_exited', models.CharField(blank=True, max_length=10)),
                ('stay_length', models.CharField(blank=True, max_length=2)),
                ('amount_charged', models.CharField(blank=True, max_length=5)),
                ('user_type', models.CharField(max_length=1)),
                ('parkingLot', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parking.Parking_Lot')),
            ],
        ),
    ]
