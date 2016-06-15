from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        CollectionSpecies = apps.get_model('species', 'CollectionSpecies')

        CollectionSpecies.objects.all().delete()

        CollectionSpeciesForm = modelform_factory(CollectionSpecies, fields='__all__')

        for r in c.execute('SELECT * FROM tbl_hash_collection_species;'):
            form = CollectionSpeciesForm(dict(collection=r[0], species=r[1], sex=r[2],
                                    count=r[3], count_estimated=r[4]))
            if form.is_valid():
                # No PK in Andre's file
                form.save()
            else:
                print('collection species', r[0:], form.errors.as_data())

    def rollback(apps, schema_editor):
        CollectionSpecies = apps.get_model('species', 'CollectionSpecies')
        CollectionSpecies.objects.all().delete()

    dependencies = [
        ('species', '0004_DATA_initial'),
        ('collections_ccdb', '0005_DATA_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
