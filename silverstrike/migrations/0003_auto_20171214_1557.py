# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0002_auto_20171214_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='recurringtransaction',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='split',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
