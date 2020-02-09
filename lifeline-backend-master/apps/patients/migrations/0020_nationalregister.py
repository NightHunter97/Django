# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-09 13:11
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import Value, CharField, F
from django.db.models.functions import Concat


def gen_national_register(apps, schema_editor):
    patients = apps.get_model('patients', 'Patient')

    national_registers = []
    patients_ids = []
    for patient in patients.objects.all():
        if not patient.national_register or patient.national_register in national_registers:
            patients_ids.append(patient.pk)
        else:
            national_registers.append(patient.national_register)

    patients.objects.filter(id__in=patients_ids).update(
        national_register=Concat(Value("INVALID_", CharField()), F('patient_id'))
    )


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0019_auto_20190328_1252'),
    ]

    operations = [
        migrations.RunPython(gen_national_register, reverse_code=migrations.RunPython.noop),
    ]
