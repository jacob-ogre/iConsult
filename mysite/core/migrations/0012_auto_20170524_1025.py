# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170523_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='date_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
