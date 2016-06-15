# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_DATA_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='region',
            field=models.ForeignKey(blank=True, related_name='sites', null=True, to='locations.Region'),
        ),
        migrations.AlterField(
            model_name='studylocation',
            name='municipal_location',
            field=models.ForeignKey(blank=True, related_name='study_locations', null=True, to='locations.MunicipalLocation'),
        ),
        migrations.AlterField(
            model_name='studylocation',
            name='site',
            field=models.ForeignKey(related_name='study_locations', to='locations.Site'),
        ),
    ]
