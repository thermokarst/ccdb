# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_remove_site_fk_dupes'),
        ('projects', '0004_initial_grantreport'),
        ('processing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADFGPermit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('number_of_traps', models.IntegerField(null=True, blank=True)),
                ('collection_start_date', models.DateField(null=True, blank=True)),
                ('collection_start_time', models.TimeField(null=True, blank=True)),
                ('collection_end_date', models.DateField(null=True, blank=True)),
                ('collection_end_time', models.TimeField(null=True, blank=True)),
                ('specimen_state', models.CharField(max_length=50, blank=True)),
                ('adfg_permit', models.ForeignKey(to='collections_ccdb.ADFGPermit', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionMethod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('collection_method_class', models.CharField(max_length=50, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='CollectionTrap',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('number_of_traps', models.IntegerField()),
                ('date_opened', models.DateField()),
                ('time_opened', models.TimeField()),
                ('date_closed', models.DateField()),
                ('time_closed', models.TimeField()),
                ('collection', models.ForeignKey(to='collections_ccdb.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='DatasheetAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('datasheet', models.FileField(verbose_name='Datasheet', upload_to='collections/datasheets/%Y/%m/%d')),
                ('collection', models.ForeignKey(to='collections_ccdb.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Flaw',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='collectiontype',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='collectionmethod',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AddField(
            model_name='collection',
            name='collection_method',
            field=models.ForeignKey(to='collections_ccdb.CollectionMethod'),
        ),
        migrations.AddField(
            model_name='collection',
            name='collection_type',
            field=models.ForeignKey(to='collections_ccdb.CollectionType'),
        ),
        migrations.AddField(
            model_name='collection',
            name='flaw',
            field=models.ForeignKey(to='collections_ccdb.Flaw', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='process_type',
            field=models.ForeignKey(to='processing.ProcessType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='collection',
            name='reagent',
            field=models.ForeignKey(to='processing.Reagent', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='storage_location',
            field=models.ForeignKey(to='locations.StorageLocation', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='study_location',
            field=models.ForeignKey(to='locations.StudyLocation'),
        ),
        migrations.AlterUniqueTogether(
            name='collectiontrap',
            unique_together=set([('collection', 'date_opened', 'time_opened', 'date_closed', 'time_closed')]),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('project', 'study_location', 'collection_type', 'collection_start_date', 'collection_end_date', 'collection_method')]),
        ),
    ]
