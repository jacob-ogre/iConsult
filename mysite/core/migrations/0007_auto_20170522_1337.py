# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default=b'<django.db.models.query_utils.DeferredAttribute object at 0x103599e50>', max_length=33),
        ),
    ]