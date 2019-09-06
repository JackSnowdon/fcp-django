# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-06 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190906_1028'),
        ('checkout', '0002_auto_20190903_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
            preserve_default=False,
        ),
    ]
