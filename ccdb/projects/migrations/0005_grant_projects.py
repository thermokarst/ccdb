# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_grant_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='projects',
            field=models.ManyToManyField(to='projects.Project', related_name='grants'),
        ),
    ]
