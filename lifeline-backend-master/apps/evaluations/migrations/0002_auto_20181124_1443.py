# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-24 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluation',
            options={'ordering': ('created',), 'verbose_name': 'Evaluation', 'verbose_name_plural': 'Evaluations'},
        ),
        migrations.AddField(
            model_name='evaluation',
            name='type',
            field=models.CharField(choices=[('income', 'Income'), ('outcome', 'Outcome')], default='income', max_length=10, verbose_name='Type'),
        ),
    ]
