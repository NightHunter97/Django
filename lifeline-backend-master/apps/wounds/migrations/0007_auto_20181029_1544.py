# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-29 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wounds', '0006_auto_20181025_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wound',
            name='localization',
            field=models.CharField(choices=[('HEAD', 'Head'), ('Neck', 'Neck'), ('THOR', 'Thorax'), ('UABD', 'Upper abdomen'), ('LABD', 'Lower abdomen'), ('LBCK', 'Upper back'), ('LBCK', 'Lower back'), ('SHDR', 'Shoulder'), ('ARM', 'Arm'), ('FORE', 'Forearm'), ('WRST', 'Wrist'), ('HAND', 'Hand'), ('GENI', 'Genital area'), ('BUTT', 'Buttock crease'), ('ING', 'Inguinal folds'), ('THGH', 'Thigh'), ('LEG', 'Leg'), ('FOOT', 'Foot')], max_length=255, verbose_name='Localization'),
        ),
    ]
