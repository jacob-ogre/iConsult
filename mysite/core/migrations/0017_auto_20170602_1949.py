# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 19:49
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170524_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='summary',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
