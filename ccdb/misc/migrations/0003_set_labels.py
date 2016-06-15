# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_DATA_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='color',
            field=models.ForeignKey(related_name='containers', blank=True, to='misc.Color', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='material',
            field=models.ForeignKey(related_name='containers', blank=True, to='misc.Material', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='measurement_unit',
            field=models.ForeignKey(related_name='containers', blank=True, to='misc.MeasurementUnit', null=True),
        ),
        migrations.AlterField(
            model_name='measurementtype',
            name='default_measurement_unit',
            field=models.ForeignKey(related_name='measurement_types', blank=True, to='misc.MeasurementUnit', null=True),
        ),
    ]
