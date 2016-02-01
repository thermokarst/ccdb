# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0001_initial'),
        ('experiments', '0005_alivedeadcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='collections',
            field=models.ManyToManyField(to='collections_ccdb.Collection'),
        ),
    ]
