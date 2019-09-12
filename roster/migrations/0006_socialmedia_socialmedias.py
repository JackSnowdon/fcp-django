# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-05 14:04
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0005_auto_20190905_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='socialmedias',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('NoSocial', 'NoSocial')], default='NoSocial', max_length=30),
        ),
    ]