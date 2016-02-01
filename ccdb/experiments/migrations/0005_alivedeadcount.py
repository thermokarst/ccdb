# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_treatment_replicate'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliveDeadCount',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('status_date', models.DateField()),
                ('status_time', models.TimeField(blank=True, null=True)),
                ('count_alive', models.IntegerField(blank=True, null=True)),
                ('count_dead', models.IntegerField(blank=True, null=True)),
                ('flaw', models.ForeignKey(to='experiments.Flaw', blank=True, null=True)),
                ('treatment_replicate', models.ForeignKey(to='experiments.TreatmentReplicate')),
            ],
        ),
    ]
