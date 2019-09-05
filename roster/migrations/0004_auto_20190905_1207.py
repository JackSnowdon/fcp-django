# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-05 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0003_auto_20190903_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wrestler',
            name='alignment',
            field=models.CharField(choices=[('Schadenfreude', 'Schadenfreude'), ('FCP', 'Fight Club: Pro')], default='FCP', max_length=32),
        ),
        migrations.DeleteModel(
            name='GoodOrBad',
        ),
    ]
