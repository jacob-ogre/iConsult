# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170522_1339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConsultBasic',
            new_name='Consultation',
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='', max_length=33),
        ),
        migrations.AlterModelTable(
            name='consultation',
            table='consultation',
        ),
    ]