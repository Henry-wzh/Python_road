# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_auto_20190624_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': '个人信息', 'verbose_name_plural': '所有信息'},
        ),
        migrations.AlterIndexTogether(
            name='person',
            index_together=set([('name', 'age')]),
        ),
    ]
