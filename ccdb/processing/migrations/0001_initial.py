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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Processing',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('container_label', models.CharField(max_length=50)),
                ('process_date', models.DateField(null=True, blank=True)),
                ('process_time', models.TimeField(null=True, blank=True)),
                ('reagent_volume', models.FloatField(null=True, blank=True)),
                ('minutes_in_reagent', models.IntegerField(null=True, blank=True)),
                ('container', models.ForeignKey(to='misc.Container')),
                ('flaw', models.ForeignKey(to='processing.Flaw', null=True, blank=True)),
                ('measurement_unit', models.ForeignKey(to='misc.MeasurementUnit', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='Reagent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('reagent_class', models.CharField(max_length=50, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
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
            field=models.ForeignKey(to='processing.Reagent', null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='processing',
            unique_together=set([('process_type', 'container', 'container_label', 'process_date', 'process_time', 'reagent')]),
        ),
        migrations.AlterField(
            model_name='processing',
            name='container',
            field=models.ForeignKey(related_name='processings', to='misc.Container'),
        ),
        migrations.AlterField(
            model_name='processing',
            name='flaw',
            field=models.ForeignKey(to='processing.Flaw', null=True, related_name='processings', blank=True),
        ),
        migrations.AlterField(
            model_name='processing',
            name='measurement_unit',
            field=models.ForeignKey(to='misc.MeasurementUnit', null=True, related_name='processings', blank=True),
        ),
        migrations.AlterField(
            model_name='processing',
            name='process_type',
            field=models.ForeignKey(related_name='processings', to='processing.ProcessType'),
        ),
        migrations.AlterField(
            model_name='processing',
            name='reagent',
            field=models.ForeignKey(to='processing.Reagent', null=True, related_name='processings', blank=True),
        ),
    ]
