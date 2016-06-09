from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        Species = apps.get_model('species', 'Species')

        Species.objects.all().delete()

        SpeciesForm = modelform_factory(Species, fields='__all__')

        for r in c.execute('SELECT * FROM tbl_lu_species;'):
            form = SpeciesForm(dict(common_name=r[1], genus=r[2],
                                    species=r[3], parasite=r[4],
                                    sort_order=int(r[5]) if r[5] else None))
            if form.is_valid():
                Species.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('species', r[0:], form.errors.as_data())

    def rollback(apps, schema_editor):
        Species = apps.get_model('species', 'Species')
        Species.objects.all().delete()

    dependencies = [
        ('species', '0003_collectionspecies'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
