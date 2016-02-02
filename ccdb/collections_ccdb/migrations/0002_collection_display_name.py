# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='display_name',
            field=models.CharField(max_length=255, editable=False, default='x'),
            preserve_default=False,
        ),
    ]
