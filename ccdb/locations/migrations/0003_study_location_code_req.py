# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_remove_site_fk_dupes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studylocation',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
