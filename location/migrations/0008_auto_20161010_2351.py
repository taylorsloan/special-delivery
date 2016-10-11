# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-10 23:51
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_auto_20161007_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='gps_location',
        ),
        migrations.AddField(
            model_name='location',
            name='position',
            field=geoposition.fields.GeopositionField(default=0, max_length=42),
            preserve_default=False,
        ),
    ]
