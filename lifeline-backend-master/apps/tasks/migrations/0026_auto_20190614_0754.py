# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-14 07:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0025_auto_20190523_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='patients.File', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='schedules', to=settings.AUTH_USER_MODEL, verbose_name='Team Members'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='tasks.Task', verbose_name='Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.Category', verbose_name='Category'),
        ),
    ]
