# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-02-01 06:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210201_0652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Data',
        ),
    ]