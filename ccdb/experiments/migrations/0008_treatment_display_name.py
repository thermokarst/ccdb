# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0007_treatment_replicates_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='display_name',
            field=models.CharField(editable=False, default='x', max_length=255),
            preserve_default=False,
        ),
    ]
