from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        CollectionType = apps.get_model('collections_ccdb', 'CollectionType')
        CollectionMethod = apps.get_model('collections_ccdb', 'CollectionMethod')
        Flaw = apps.get_model('collections_ccdb', 'Flaw')
        ADFGPermit = apps.get_model('collections_ccdb', 'ADFGPermit')
        Collection = apps.get_model('collections_ccdb', 'Collection')
        DatasheetAttachment = apps.get_model('collections_ccdb', 'DatasheetAttachment')
        CollectionTrap = apps.get_model('collections_ccdb', 'CollectionTrap')

        for model in [CollectionTrap, Collection, Flaw, DatasheetAttachment,
                      CollectionMethod, CollectionType, ADFGPermit]:
            model.objects.all().delete()

        Project = apps.get_model('projects', 'Project')

        CollectionTypeForm = modelform_factory(CollectionType, fields='__all__')
        CollectionMethodForm = modelform_factory(CollectionMethod, fields='__all__')
        ADFGPermitForm = modelform_factory(ADFGPermit, fields='__all__')
        CollectionForm = modelform_factory(Collection, fields='__all__')

        for r in c.execute('SELECT * FROM tbl_lu_collection_types;'):
            form = CollectionTypeForm(dict(name=r[1], code=r[2],
                                           sort_order=int(r[3]) if r[3] else None))
            if form.is_valid():
                CollectionType.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('collection type', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_collection_methods;'):
            form = CollectionMethodForm(dict(name=r[1], code=r[2],
                                             collection_method_class=r[3],
                                             sort_order=int(r[4]) if r[4] else None))
            if form.is_valid():
                CollectionMethod.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('collection method', r[0:], form.errors.as_data())

        for i, r in enumerate(c.execute('SELECT DISTINCT ADFG_Permit FROM tbl_collections;')):
            form = ADFGPermitForm(dict(name=r[0], sort_order=i))
            if form.is_valid():
                form.save()
            else:
                print('adfg permit', r[0:], form.errors.as_data())

        for r in c.execute('''
                SELECT *,
                    collection_start_date AS "collection_start_date [dtdt]",
                    collection_start_time AS "collection_start_time [dtdt]",
                    collection_end_date   AS "collection_end_date [dtdt]",
                    collection_end_time   AS "collection_end_time [dtdt]"
                FROM tbl_collections;
                '''):
            permit = None
            if r[14] is not '':
                permit = ADFGPermit.objects.get(name=r[14]).pk
            form = CollectionForm(dict(project=r[0], study_location=r[2],
                                       collection_type=r[3], collection_method=r[4],
                                       number_of_traps=r[5],
                                       collection_start_date=r[17],
                                       collection_start_time=r[18].time() if r[18] else None,
                                       collection_end_date=r[19],
                                       collection_end_time=r[20].time() if r[20] else None,
                                       storage_location=r[10], specimen_state=r[11],
                                       process_type=r[12], reagent=r[13],
                                       adfg_permit=permit))
            if form.is_valid():
                project = Project.objects.get(id=r[0])
                d = "{}_{}_{}_{}".format(project, form.cleaned_data['collection_end_date'],
                                         form.cleaned_data['study_location'],
                                         form.cleaned_data['collection_type'])
                Collection.objects.create(id=r[1], display_name=d, **form.cleaned_data)
            else:
                print('collection', r[0:], form.errors.as_data())

    def rollback(apps, schema_editor):
        CollectionType = apps.get_model('collections_ccdb', 'CollectionType')
        CollectionMethod = apps.get_model('collections_ccdb', 'CollectionMethod')
        Flaw = apps.get_model('collections_ccdb', 'Flaw')
        ADFGPermit = apps.get_model('collections_ccdb', 'ADFGPermit')
        Collection = apps.get_model('collections_ccdb', 'Collection')
        DatasheetAttachment = apps.get_model('collections_ccdb', 'DatasheetAttachment')
        CollectionTrap = apps.get_model('collections_ccdb', 'CollectionTrap')

        for model in [CollectionTrap, Collection, Flaw, DatasheetAttachment,
                      CollectionMethod, CollectionType, ADFGPermit]:
            model.objects.all().delete()

    dependencies = [
        ('collections_ccdb', '0004_collections_ordering'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
