# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-21 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ngo', '0004_auto_20180221_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='users',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]