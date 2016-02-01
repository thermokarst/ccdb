# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150)),
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
            name='Flaw',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
            name='ProtocolAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
    ]
