# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0003_collections_ordering'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adfgpermit',
            options={'ordering': ['sort_order'], 'verbose_name': 'ADFG Permit'},
        ),
    ]
