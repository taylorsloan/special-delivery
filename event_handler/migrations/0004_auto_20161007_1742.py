# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-07 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_handler', '0003_auto_20161007_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='device_id',
            new_name='device',
        ),
    ]