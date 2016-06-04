# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160601_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='links',
        ),
        migrations.AddField(
            model_name='menulink',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu'),
        ),
    ]