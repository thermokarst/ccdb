# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('common_name', models.CharField(max_length=100)),
                ('genus', models.CharField(max_length=50, blank=True)),
                ('species', models.CharField(max_length=50, blank=True)),
                ('parasite', models.BooleanField(default=False)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='common_name')),
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
    ]
