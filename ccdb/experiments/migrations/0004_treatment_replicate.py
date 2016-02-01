# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_treatment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentReplicate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('setup_date', models.DateField(null=True, blank=True)),
                ('setup_time', models.TimeField(null=True, blank=True)),
                ('setup_sample_size', models.IntegerField(null=True, blank=True)),
                ('mass_g', models.FloatField(null=True, blank=True)),
                ('flaw', models.ForeignKey(null=True, to='experiments.Flaw', blank=True)),
                ('treatment', models.ForeignKey(to='experiments.Treatment')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='treatmentreplicate',
            unique_together=set([('treatment', 'name', 'setup_date', 'setup_time')]),
        ),
    ]
