# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20170524_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
    ]