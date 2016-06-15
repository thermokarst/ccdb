# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_DATA_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantreport',
            name='grant',
            field=models.ForeignKey(to='projects.Grant', related_name='reports'),
        ),
    ]
