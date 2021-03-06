# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170523_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='area_unit',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='summary',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='title',
            field=models.CharField(default='', max_length=150),
        ),
    ]
