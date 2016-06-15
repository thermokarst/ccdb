# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0005_DATA_species_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionspecies',
            name='collection',
            field=models.ForeignKey(related_name='collection_species', to='collections_ccdb.Collection'),
        ),
        migrations.AlterField(
            model_name='collectionspecies',
            name='species',
            field=models.ForeignKey(related_name='collection_species', to='species.Species'),
        ),
        migrations.AlterField(
            model_name='trapspecies',
            name='collection_trap',
            field=models.ForeignKey(related_name='trap_species', to='collections_ccdb.CollectionTrap'),
        ),
        migrations.AlterField(
            model_name='trapspecies',
            name='species',
            field=models.ForeignKey(related_name='trap_species', to='species.Species'),
        ),
    ]
