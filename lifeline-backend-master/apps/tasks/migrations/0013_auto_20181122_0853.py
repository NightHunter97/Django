# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-22 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20181114_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='Team Members'),
        ),
    ]
