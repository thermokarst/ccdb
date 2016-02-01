# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=25, blank=True)),
                ('treatment_type', models.CharField(max_length=50, blank=True)),
                ('placement', models.CharField(max_length=25, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('experiment', models.ForeignKey(null=True, blank=True, to='experiments.Experiment')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='treatmenttype',
            unique_together=set([('experiment', 'name')]),
        ),
    ]
