# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0002_DATA_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processing',
            name='container',
            field=models.ForeignKey(related_name='processings', to='misc.Container'),
        ),
        migrations.AlterField(
            model_name='processing',
            name='flaw',
            field=models.ForeignKey(to='processing.Flaw', blank=True, related_name='processings', null=True),
        ),
        migrations.AlterField(
            model_name='processing',
            name='measurement_unit',
            field=models.ForeignKey(to='misc.MeasurementUnit', blank=True, related_name='processings', null=True),
        ),
        migrations.AlterField(
            model_name='processing',
            name='process_type',
            field=models.ForeignKey(related_name='processings', to='processing.ProcessType'),
        ),
        migrations.AlterField(
            model_name='processing',
            name='reagent',
            field=models.ForeignKey(to='processing.Reagent', blank=True, related_name='processings', null=True),
        ),
    ]
