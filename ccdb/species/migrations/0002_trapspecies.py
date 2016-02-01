# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0001_initial'),
        ('species', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrapSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('sex', models.CharField(blank=True, max_length=25)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('count_estimated', models.BooleanField(default=False)),
                ('collection_trap', models.ForeignKey(to='collections_ccdb.CollectionTrap')),
                ('species', models.ForeignKey(to='species.Species')),
            ],
            options={
                'verbose_name_plural': 'trap-species',
            },
        ),
    ]
