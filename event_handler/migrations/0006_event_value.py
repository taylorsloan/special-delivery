# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-05 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_handler', '0005_auto_20161014_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='value',
            field=models.CharField(max_length=10, null=True),
        ),
    ]