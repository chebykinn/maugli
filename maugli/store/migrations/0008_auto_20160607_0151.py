# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_titlecolumn_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricecolumn',
            name='type',
        ),
        migrations.RemoveField(
            model_name='titlecolumn',
            name='type',
        ),
    ]
