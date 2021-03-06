# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-16 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20181219_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note header'),
        ),
        migrations.AddField(
            model_name='journal',
            name='name_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note header'),
        ),
        migrations.AddField(
            model_name='journal',
            name='name_nl',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note header'),
        ),
    ]
