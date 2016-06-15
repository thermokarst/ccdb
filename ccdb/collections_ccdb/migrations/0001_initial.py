from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0002_DATA_initial'),
        ('processing', '0001_initial'),
        ('locations', '0002_DATA_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADFGPermit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number_of_traps', models.IntegerField(blank=True, null=True)),
                ('collection_start_date', models.DateField(blank=True, null=True)),
                ('collection_start_time', models.TimeField(blank=True, null=True)),
                ('collection_end_date', models.DateField(blank=True, null=True)),
                ('collection_end_time', models.TimeField(blank=True, null=True)),
                ('specimen_state', models.CharField(blank=True, max_length=50)),
                ('adfg_permit', models.ForeignKey(blank=True, null=True, to='collections_ccdb.ADFGPermit')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('collection_method_class', models.CharField(blank=True, max_length=50)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='CollectionTrap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='DatasheetAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('datasheet', models.FileField(upload_to='collections/datasheets/%Y/%m/%d', verbose_name='Datasheet')),
                ('collection', models.ForeignKey(to='collections_ccdb.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Flaw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
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
            field=models.ForeignKey(blank=True, null=True, to='collections_ccdb.Flaw'),
        ),
        migrations.AddField(
            model_name='collection',
            name='process_type',
            field=models.ForeignKey(blank=True, null=True, to='processing.ProcessType'),
        ),
        migrations.AddField(
            model_name='collection',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='collection',
            name='reagent',
            field=models.ForeignKey(blank=True, null=True, to='processing.Reagent'),
        ),
        migrations.AddField(
            model_name='collection',
            name='storage_location',
            field=models.ForeignKey(blank=True, null=True, to='locations.StorageLocation'),
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
        migrations.AddField(
            model_name='collection',
            name='display_name',
            field=models.CharField(editable=False, default='x', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['project', 'collection_end_date']},
        ),
        migrations.AlterModelOptions(
            name='adfgpermit',
            options={'ordering': ['sort_order'], 'verbose_name': 'ADFG Permit'},
        ),
        migrations.AlterField(
            model_name='collection',
            name='adfg_permit',
            field=models.ForeignKey(related_name='collections', blank=True, null=True, to='collections_ccdb.ADFGPermit'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_method',
            field=models.ForeignKey(related_name='collections', to='collections_ccdb.CollectionMethod'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_type',
            field=models.ForeignKey(related_name='collections', to='collections_ccdb.CollectionType'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='flaw',
            field=models.ForeignKey(related_name='collections', blank=True, null=True, to='collections_ccdb.Flaw'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='process_type',
            field=models.ForeignKey(related_name='collections', blank=True, null=True, to='processing.ProcessType'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='project',
            field=models.ForeignKey(related_name='collections', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='reagent',
            field=models.ForeignKey(related_name='collections', blank=True, null=True, to='processing.Reagent'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='storage_location',
            field=models.ForeignKey(related_name='collections', blank=True, null=True, to='locations.StorageLocation'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='study_location',
            field=models.ForeignKey(related_name='collections', to='locations.StudyLocation'),
        ),
        migrations.AlterField(
            model_name='collectiontrap',
            name='collection',
            field=models.ForeignKey(related_name='traps', to='collections_ccdb.Collection'),
        ),
        migrations.AlterField(
            model_name='datasheetattachment',
            name='collection',
            field=models.ForeignKey(related_name='datasheets', to='collections_ccdb.Collection'),
        ),
    ]
