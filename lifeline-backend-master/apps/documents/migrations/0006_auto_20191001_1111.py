# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-01 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0031_auto_20190619_1213'),
        ('documents', '0005_remove_document_preview_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='patient',
        ),
        migrations.AddField(
            model_name='document',
            name='patient_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.File'),
        ),
    ]
