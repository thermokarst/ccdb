# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0010_DATA_collections_experiments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alivedeadcount',
            name='flaw',
            field=models.ForeignKey(null=True, to='experiments.Flaw', related_name='alive_dead_counts', blank=True),
        ),
        migrations.AlterField(
            model_name='alivedeadcount',
            name='treatment_replicate',
            field=models.ForeignKey(to='experiments.TreatmentReplicate', related_name='alive_dead_counts'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='flaw',
            field=models.ForeignKey(null=True, to='experiments.Flaw', related_name='experiments', blank=True),
        ),
        migrations.AlterField(
            model_name='protocolattachment',
            name='experiment',
            field=models.ForeignKey(to='experiments.Experiment', related_name='protocols'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='container',
            field=models.ForeignKey(null=True, to='misc.Container', related_name='treatments', blank=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='flaw',
            field=models.ForeignKey(null=True, to='experiments.Flaw', related_name='treatments', blank=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='species',
            field=models.ForeignKey(to='species.Species', related_name='treatments'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='study_location',
            field=models.ForeignKey(to='locations.StudyLocation', related_name='treatments'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='treatment_type',
            field=models.ForeignKey(to='experiments.TreatmentType', related_name='treatments'),
        ),
        migrations.AlterField(
            model_name='treatmentreplicate',
            name='flaw',
            field=models.ForeignKey(null=True, to='experiments.Flaw', related_name='treatment_replicates', blank=True),
        ),
        migrations.AlterField(
            model_name='treatmentreplicate',
            name='treatment',
            field=models.ForeignKey(to='experiments.Treatment', related_name='treatment_replicates'),
        ),
        migrations.AlterField(
            model_name='treatmenttype',
            name='experiment',
            field=models.ForeignKey(null=True, to='experiments.Experiment', related_name='treatment_types', blank=True),
        ),
    ]
