# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-02-02 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('help', models.CharField(max_length=500)),
            ],
        ),
    ]