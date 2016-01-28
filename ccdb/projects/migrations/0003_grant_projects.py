# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial_grant'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='projects',
            field=models.ManyToManyField(to='projects.Project', related_name='grants'),
        ),
    ]
