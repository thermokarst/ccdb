from django.db import migrations

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        Collection = apps.get_model('collections_ccdb', 'Collection')
        Experiment = apps.get_model('experiments', 'Experiment')

        for experiment in Experiment.objects.all():
            experiment.collections.all().delete()

        for r in c.execute('SELECT * FROM tbl_hash_collection_experiments;'):
            c = Collection.objects.get(id=r[0])
            e = Experiment.objects.get(id=r[1])
            e.collections.add(c)
            e.save()

    def rollback(apps, schema_editor):
        Experiment = apps.get_model('experiments', 'Experiment')

        for experiment in Experiment.objects.all():
            experiment.collections.all().delete()

    dependencies = [
        ('experiments', '0009_DATA_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
