# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-04 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0006_collection_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_measured', models.DateField()),
                ('time_measured', models.TimeField()),
                ('water_temp_c', models.FloatField(null=True)),
                ('air_temp_c', models.FloatField(null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='env_measurements', to='collections_ccdb.Collection')),
            ],
            options={
                'ordering': ['date_measured', 'time_measured'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='collectionmeasurement',
            unique_together=set([('collection', 'date_measured', 'time_measured')]),
        ),
    ]
