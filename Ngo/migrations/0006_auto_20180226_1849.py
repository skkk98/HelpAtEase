# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-26 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ngo', '0005_auto_20180221_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
