# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
        ('species', '0003_collectionspecies'),
        ('locations', '0002_remove_site_fk_dupes'),
        ('experiments', '0002_treatment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('sex', models.CharField(max_length=25)),
                ('container', models.ForeignKey(blank=True, null=True, to='misc.Container')),
                ('flaw', models.ForeignKey(blank=True, null=True, to='experiments.Flaw')),
                ('species', models.ForeignKey(to='species.Species')),
                ('study_location', models.ForeignKey(to='locations.StudyLocation')),
                ('treatment_type', models.ForeignKey(to='experiments.TreatmentType')),
            ],
        ),
    ]
