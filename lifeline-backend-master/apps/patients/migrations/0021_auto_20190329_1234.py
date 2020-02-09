# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-29 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0020_nationalregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='national_register',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='National Register'),
        ),
    ]
