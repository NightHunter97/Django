# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-23 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('evaluations', '0008_evaluation_results_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='survey_groups',
            field=models.ManyToManyField(blank=True, related_name='surveys', to='auth.Group', verbose_name='Groups'),
        ),
    ]
