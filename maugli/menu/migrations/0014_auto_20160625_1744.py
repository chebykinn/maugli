# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-25 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_remove_menulink_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulink',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
