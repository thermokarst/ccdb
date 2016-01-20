# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('sort_order', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='grant',
            unique_together=set([('title', 'code')]),
        ),
    ]
