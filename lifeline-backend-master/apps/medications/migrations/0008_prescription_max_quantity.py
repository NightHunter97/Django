# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-12 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0007_auto_20190312_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='max_quantity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Maximum posology per day (Co/day)'),
        ),
    ]
