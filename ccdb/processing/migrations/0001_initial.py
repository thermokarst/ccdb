# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flaw',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Processing',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('container_label', models.CharField(max_length=50)),
                ('process_date', models.DateField(blank=True, null=True)),
                ('process_time', models.TimeField(blank=True, null=True)),
                ('reagent_volume', models.FloatField(blank=True, null=True)),
                ('minutes_in_reagent', models.IntegerField(blank=True, null=True)),
                ('container', models.ForeignKey(to='misc.Container')),
                ('flaw', models.ForeignKey(to='processing.Flaw', blank=True, null=True)),
                ('measurement_unit', models.ForeignKey(to='misc.MeasurementUnit', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Reagent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('reagent_class', models.CharField(blank=True, max_length=50)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='reagent',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='processtype',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AddField(
            model_name='processing',
            name='process_type',
            field=models.ForeignKey(to='processing.ProcessType'),
        ),
        migrations.AddField(
            model_name='processing',
            name='reagent',
            field=models.ForeignKey(to='processing.Reagent', blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='processing',
            unique_together=set([('process_type', 'container', 'container_label', 'process_date', 'process_time', 'reagent')]),
        ),
    ]
