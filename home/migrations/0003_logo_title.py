# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-17 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='title',
            field=models.CharField(default='', max_length=254),
        ),
    ]
