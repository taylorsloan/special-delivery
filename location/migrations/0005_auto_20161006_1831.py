# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-06 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20161005_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('-timestamp',)},
        ),
    ]