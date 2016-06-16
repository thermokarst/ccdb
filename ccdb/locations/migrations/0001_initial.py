from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MunicipalLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('municipal_location_type', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('region', models.ForeignKey(to='locations.Region', null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('facility', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('room', models.CharField(blank=True, max_length=50)),
                ('freezer', models.CharField(blank=True, max_length=50)),
                ('temp_c', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='StudyLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10)),
                ('study_location_type', models.CharField(blank=True, max_length=50)),
                ('treatment_type', models.CharField(blank=True, max_length=100)),
                ('collecting_location', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('municipal_location', models.ForeignKey(to='locations.MunicipalLocation', null=True, blank=True)),
                ('site', models.ForeignKey(to='locations.Site', null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='site',
            unique_together=set([('region', 'name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='municipallocation',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='storagelocation',
            unique_together=set([('code', 'facility', 'building', 'room',
                                  'freezer', 'temp_c')]),
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='studylocation',
            unique_together=set([('site', 'name')]),
        ),
        migrations.AlterField(
            model_name='studylocation',
            name='site',
            field=models.ForeignKey(to='locations.Site'),
        ),
        migrations.AlterField(
            model_name='studylocation',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='site',
            name='region',
            field=models.ForeignKey(to='locations.Region', null=True, blank=True, related_name='sites'),
        ),
        migrations.AlterField(
            model_name='studylocation',
            name='municipal_location',
            field=models.ForeignKey(to='locations.MunicipalLocation', null=True, blank=True, related_name='study_locations'),
        ),
        migrations.AlterField(
            model_name='studylocation',
            name='site',
            field=models.ForeignKey(to='locations.Site', related_name='study_locations'),
        ),
    ]
