# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_grant_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrantReport',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('report_type', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('submitted_date', models.DateField(blank=True, null=True)),
                ('attachment', models.FileField(upload_to='projects/grants/grant_report_attachments/%Y/%m/%d', blank=True, null=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('grant', models.ForeignKey(to='projects.Grant')),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
    ]
