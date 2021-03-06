# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-10 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0022_auto_20190910_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='unit',
        ),
        migrations.AddField(
            model_name='prescription',
            name='duration_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Duration end'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='duration_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Duration start'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='comment',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='duration',
            field=models.CharField(blank=True, choices=[('INDEF', 'Indefinite'), ('FIXED', 'Fixed')], default='INDEF', max_length=5, null=True, verbose_name='Duration'),
        ),
    ]
