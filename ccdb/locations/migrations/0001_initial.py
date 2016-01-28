# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipalLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('municipal_location_type', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('region', models.ForeignKey(to='locations.Region', null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facility', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=50, blank=True)),
                ('freezer', models.CharField(max_length=50, blank=True)),
                ('temp_c', models.IntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='StudyLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('study_location_type', models.CharField(max_length=50, blank=True)),
                ('treatment_type', models.CharField(max_length=100, blank=True)),
                ('collecting_location', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('municipal_location', models.ForeignKey(to='locations.MunicipalLocation', null=True, blank=True)),
                ('site', models.ForeignKey(to='locations.Site', null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AddField(
            model_name='municipallocation',
            name='site',
            field=models.ForeignKey(to='locations.Site'),
        ),
        migrations.AlterUniqueTogether(
            name='studylocation',
            unique_together=set([('site', 'name')]),
        ),
    ]
