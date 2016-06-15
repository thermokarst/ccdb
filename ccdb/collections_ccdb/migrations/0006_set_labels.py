# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_ccdb', '0005_DATA_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='adfg_permit',
            field=models.ForeignKey(null=True, related_name='collections', to='collections_ccdb.ADFGPermit', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_method',
            field=models.ForeignKey(to='collections_ccdb.CollectionMethod', related_name='collections'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_type',
            field=models.ForeignKey(to='collections_ccdb.CollectionType', related_name='collections'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='flaw',
            field=models.ForeignKey(null=True, related_name='collections', to='collections_ccdb.Flaw', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='process_type',
            field=models.ForeignKey(null=True, related_name='collections', to='processing.ProcessType', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='project',
            field=models.ForeignKey(to='projects.Project', related_name='collections'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='reagent',
            field=models.ForeignKey(null=True, related_name='collections', to='processing.Reagent', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='storage_location',
            field=models.ForeignKey(null=True, related_name='collections', to='locations.StorageLocation', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='study_location',
            field=models.ForeignKey(to='locations.StudyLocation', related_name='collections'),
        ),
        migrations.AlterField(
            model_name='collectiontrap',
            name='collection',
            field=models.ForeignKey(to='collections_ccdb.Collection', related_name='traps'),
        ),
        migrations.AlterField(
            model_name='datasheetattachment',
            name='collection',
            field=models.ForeignKey(to='collections_ccdb.Collection', related_name='datasheets'),
        ),
    ]
