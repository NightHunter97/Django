# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-22 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0009_auto_20190314_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='dosage',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='dosage',
        ),
    ]
