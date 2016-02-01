# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipallocation',
            name='site',
        ),
        migrations.AlterField(
            model_name='studylocation',
            name='site',
            field=models.ForeignKey(to='locations.Site'),
        ),
    ]
