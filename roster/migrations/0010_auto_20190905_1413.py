# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-05 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0009_auto_20190905_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='wrestler',
            name='instagram_handle',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='wrestler',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
