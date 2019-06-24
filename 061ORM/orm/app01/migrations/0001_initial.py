# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('birth', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
