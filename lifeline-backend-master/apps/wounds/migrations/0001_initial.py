# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import lifeline.storage_backends


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('width', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Width')),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Height')),
                ('photo', models.ImageField(max_length=255, storage=lifeline.storage_backends.PrivateMediaStorage(), upload_to='', verbose_name='Wound photo')),
            ],
            options={
                'verbose_name': 'Evolution',
                'verbose_name_plural': 'Evolutions',
                'db_table': 'wound_evolution',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Wound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Wound name')),
                ('type', models.CharField(choices=[('OPEN', 'Open wound'), ('SUTU', 'Sutured wound'), ('SORE', 'Decubitus ulcer/pressure sore'), ('TRAU', 'Traumatic wound'), ('SKIN', 'Skin graft wound'), ('OPER', 'Post-operative wound'), ('DRAI', 'Post-drainage wound'), ('BURN', 'Burn'), ('ABSC', 'Abscess'), ('ULCR', 'Ulcer'), ('PERI', 'Periphlebitis'), ('LESI', 'Skin lesion'), ('FIST', 'Arteriovenous fistula'), ('SPRA', 'Sprain'), ('CONT', 'Contusion'), ('HAEM', 'Haematoma')], max_length=255, verbose_name='Wound type')),
                ('localization', models.CharField(choices=[('HEAD', 'Head'), ('HAND', 'Hand'), ('LEG', 'Leg'), ('BODY', 'Body')], max_length=255, verbose_name='Localization')),
                ('is_cured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Wound',
                'verbose_name_plural': 'Wounds',
                'db_table': 'wounds',
            },
        ),
        migrations.AddField(
            model_name='evolution',
            name='wound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wounds.Wound', verbose_name='Wound'),
        ),
    ]
