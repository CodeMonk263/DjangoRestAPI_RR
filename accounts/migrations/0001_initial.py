# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2021-02-01 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Data',
                'verbose_name_plural': 'Data',
            },
        ),
    ]
