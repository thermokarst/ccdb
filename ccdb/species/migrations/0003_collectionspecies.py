# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0001_initial'),
        ('species', '0002_trapspecies'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionSpecies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sex', models.CharField(blank=True, max_length=25)),
                ('count', models.IntegerField(null=True, blank=True)),
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
    ]
