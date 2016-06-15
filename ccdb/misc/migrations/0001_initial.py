from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('color_number', models.FloatField(blank=True, null=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('application', models.CharField(max_length=50, blank=True)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('color', models.ForeignKey(blank=True, to='misc.Color', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('material_class', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='MeasurementType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('measurement_type_class', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=25)),
                ('unit_class', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='measurementunit',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AddField(
            model_name='measurementtype',
            name='default_measurement_unit',
            field=models.ForeignKey(blank=True, to='misc.MeasurementUnit', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='material',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AddField(
            model_name='container',
            name='material',
            field=models.ForeignKey(blank=True, to='misc.Material', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='measurement_unit',
            field=models.ForeignKey(blank=True, to='misc.MeasurementUnit', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='color',
            unique_together=set([('name', 'code', 'color_number')]),
        ),
        migrations.AlterField(
            model_name='container',
            name='color',
            field=models.ForeignKey(blank=True, to='misc.Color', related_name='containers', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='material',
            field=models.ForeignKey(blank=True, to='misc.Material', related_name='containers', null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='measurement_unit',
            field=models.ForeignKey(blank=True, to='misc.MeasurementUnit', related_name='containers', null=True),
        ),
        migrations.AlterField(
            model_name='measurementtype',
            name='default_measurement_unit',
            field=models.ForeignKey(blank=True, to='misc.MeasurementUnit', related_name='measurement_types', null=True),
        ),
    ]
