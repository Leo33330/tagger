# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20170410_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='interop_id',
            field=models.IntegerField(default=0),
        ),
    ]