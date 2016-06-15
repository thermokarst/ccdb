from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):
    dependencies = [
        ('collections_ccdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('common_name', models.CharField(max_length=100)),
                ('genus', models.CharField(max_length=50, blank=True)),
                ('species', models.CharField(max_length=50, blank=True)),
                ('parasite', models.BooleanField(default=False)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='common_name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
                'verbose_name_plural': 'species',
            },
        ),
        migrations.AlterUniqueTogether(
            name='species',
            unique_together=set([('common_name', 'species')]),
        ),
        migrations.CreateModel(
            name='TrapSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sex', models.CharField(max_length=25, blank=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('count_estimated', models.BooleanField(default=False)),
                ('collection_trap', models.ForeignKey(to='collections_ccdb.CollectionTrap')),
                ('species', models.ForeignKey(to='species.Species')),
            ],
            options={
                'verbose_name_plural': 'trap-species',
            },
        ),
        migrations.CreateModel(
            name='CollectionSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sex', models.CharField(max_length=25, blank=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('count_estimated', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(to='collections_ccdb.Collection')),
                ('species', models.ForeignKey(to='species.Species')),
            ],
            options={
                'verbose_name_plural': 'collection-species',
            },
        ),
        migrations.AlterUniqueTogether(
            name='collectionspecies',
            unique_together=set([('collection', 'species')]),
        ),
        migrations.AlterField(
            model_name='collectionspecies',
            name='collection',
            field=models.ForeignKey(to='collections_ccdb.Collection', related_name='collection_species'),
        ),
        migrations.AlterField(
            model_name='collectionspecies',
            name='species',
            field=models.ForeignKey(to='species.Species', related_name='collection_species'),
        ),
        migrations.AlterField(
            model_name='trapspecies',
            name='collection_trap',
            field=models.ForeignKey(to='collections_ccdb.CollectionTrap', related_name='trap_species'),
        ),
        migrations.AlterField(
            model_name='trapspecies',
            name='species',
            field=models.ForeignKey(to='species.Species', related_name='trap_species'),
        ),
    ]
