# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170523_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='species',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='summary',
            field=models.TextField(blank=True, default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='title',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]