from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):
    dependencies = [
        ('misc', '0001_initial'),
        ('locations', '0001_initial'),
        ('collections_ccdb', '0001_initial'),
        ('species', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
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
            name='Flaw',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
            name='ProtocolAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('protocol', models.FileField(upload_to='experiments/protocols/%Y/%m/%d')),
                ('experiment', models.ForeignKey(to='experiments.Experiment')),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='flaw',
            field=models.ForeignKey(to='experiments.Flaw', null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='experiment',
            unique_together=set([('name', 'code')]),
        ),
        migrations.CreateModel(
            name='TreatmentType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(blank=True, max_length=25)),
                ('treatment_type', models.CharField(blank=True, max_length=50)),
                ('placement', models.CharField(blank=True, max_length=25)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('experiment', models.ForeignKey(to='experiments.Experiment', null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='treatmenttype',
            unique_together=set([('experiment', 'name')]),
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sex', models.CharField(max_length=25)),
                ('container', models.ForeignKey(to='misc.Container', null=True, blank=True)),
                ('flaw', models.ForeignKey(to='experiments.Flaw', null=True, blank=True)),
                ('species', models.ForeignKey(to='species.Species')),
                ('study_location', models.ForeignKey(to='locations.StudyLocation')),
                ('treatment_type', models.ForeignKey(to='experiments.TreatmentType')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentReplicate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('setup_date', models.DateField(blank=True, null=True)),
                ('setup_time', models.TimeField(blank=True, null=True)),
                ('setup_sample_size', models.IntegerField(blank=True, null=True)),
                ('mass_g', models.FloatField(blank=True, null=True)),
                ('flaw', models.ForeignKey(to='experiments.Flaw', null=True, blank=True)),
                ('treatment', models.ForeignKey(to='experiments.Treatment')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='treatmentreplicate',
            unique_together=set([('treatment', 'name', 'setup_date', 'setup_time')]),
        ),
        migrations.CreateModel(
            name='AliveDeadCount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('status_date', models.DateField()),
                ('status_time', models.TimeField(blank=True, null=True)),
                ('count_alive', models.IntegerField(blank=True, null=True)),
                ('count_dead', models.IntegerField(blank=True, null=True)),
                ('flaw', models.ForeignKey(to='experiments.Flaw', null=True, blank=True)),
                ('treatment_replicate', models.ForeignKey(to='experiments.TreatmentReplicate')),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='collections',
            field=models.ManyToManyField(to='collections_ccdb.Collection'),
        ),
        migrations.AlterModelOptions(
            name='alivedeadcount',
            options={'verbose_name': 'Alive-dead Count'},
        ),
        migrations.AddField(
            model_name='treatmentreplicate',
            name='display_name',
            field=models.CharField(default='x', max_length=255, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treatment',
            name='display_name',
            field=models.CharField(default='x', max_length=255, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alivedeadcount',
            name='flaw',
            field=models.ForeignKey(related_name='alive_dead_counts', to='experiments.Flaw', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='alivedeadcount',
            name='treatment_replicate',
            field=models.ForeignKey(related_name='alive_dead_counts', to='experiments.TreatmentReplicate'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='flaw',
            field=models.ForeignKey(related_name='experiments', to='experiments.Flaw', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='protocolattachment',
            name='experiment',
            field=models.ForeignKey(related_name='protocols', to='experiments.Experiment'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='container',
            field=models.ForeignKey(related_name='treatments', to='misc.Container', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='flaw',
            field=models.ForeignKey(related_name='treatments', to='experiments.Flaw', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='species',
            field=models.ForeignKey(related_name='treatments', to='species.Species'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='study_location',
            field=models.ForeignKey(related_name='treatments', to='locations.StudyLocation'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treatment_type',
            field=models.ForeignKey(related_name='treatments', to='experiments.TreatmentType'),
        ),
        migrations.AlterField(
            model_name='treatmentreplicate',
            name='flaw',
            field=models.ForeignKey(related_name='treatment_replicates', to='experiments.Flaw', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='treatmentreplicate',
            name='treatment',
            field=models.ForeignKey(related_name='treatment_replicates', to='experiments.Treatment'),
        ),
        migrations.AlterField(
            model_name='treatmenttype',
            name='experiment',
            field=models.ForeignKey(related_name='treatment_types', to='experiments.Experiment', null=True, blank=True),
        ),
    ]
