# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.BooleanField(choices=[(0, 'female'), (1, 'male')], verbose_name='性别'),
        ),
    ]
