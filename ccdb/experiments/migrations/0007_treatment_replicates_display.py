# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0006_experiment_collections'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alivedeadcount',
            options={'verbose_name': 'Alive-dead Count'},
        ),
        migrations.AddField(
            model_name='treatmentreplicate',
            name='display_name',
            field=models.CharField(editable=False, max_length=255, default='x'),
            preserve_default=False,
        ),
    ]
