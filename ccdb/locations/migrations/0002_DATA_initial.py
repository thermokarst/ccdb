from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        Region = apps.get_model('locations', 'Region')
        Site = apps.get_model('locations', 'Site')
        MunicipalLocation = apps.get_model('locations', 'MunicipalLocation')
        StudyLocation = apps.get_model('locations', 'StudyLocation')
        StorageLocation = apps.get_model('locations', 'StorageLocation')

        for model in [StorageLocation, StudyLocation, MunicipalLocation, Site, Region]:
            model.objects.all().delete()

        RegionForm = modelform_factory(Region, fields='__all__')
        SiteForm = modelform_factory(Site, fields='__all__')
        MunicipalLocationForm = modelform_factory(MunicipalLocation, fields='__all__')
        StudyLocationForm = modelform_factory(StudyLocation, fields='__all__')
        StorageLocationForm = modelform_factory(StorageLocation, fields='__all__')

        for r in c.execute('SELECT * FROM tbl_lu_regions;'):
            form = RegionForm(dict(name=r[1], code=r[2],
                                   sort_order=int(r[3]) if r[3] else None))
            if form.is_valid():
                Region.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('region', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_sites;'):
            form = SiteForm(dict(region=r[0], name=r[2], code=r[3],
                                 description=r[4],
                                 sort_order=int(r[5]) if r[5] else None))
            if form.is_valid():
                Site.objects.create(id=r[1], **form.cleaned_data)
            else:
                print('site', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_municipal_locations;'):
            form = MunicipalLocationForm(dict(name=r[2], code=r[3],
                                              municipal_location_type=r[4],
                                              description=r[5],
                                              sort_order=int(r[6]) if r[6] else None))
            if form.is_valid():
                MunicipalLocation.objects.create(id=r[1], **form.cleaned_data)
            else:
                print('municipal location', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_study_locations;'):
            form = StudyLocationForm(dict(site=r[0], name=r[2], code=r[3],
                                          study_location_type=r[4],
                                          treatment_type=r[5],
                                          municipal_location=r[6],
                                          collection_location=r[7],
                                          description=r[13],
                                          sort_order=int(r[14]) if r[14] else None))
            if form.is_valid():
                StudyLocation.objects.create(id=r[1], **form.cleaned_data)
            else:
                print('study location', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_storage_locations;'):
            bldg = ''.join(e[0].upper() for e in r[2].split())
            temp_c = r[5] if r[5] else '20'
            freezer = r[4] if r[4] else 'No Freezer'
            code = ' '.join([bldg, str(temp_c)+'C', str(freezer)])
            form = StorageLocationForm(dict(facility=r[1], building=r[2], room=r[3],
                                            freezer=r[4],
                                            temp_c=int(r[5]) if r[5] else None,
                                            code=code,
                                            description=r[6],
                                            sort_order=int(r[7]) if r[7] else None))
            if form.is_valid():
                StorageLocation.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('storage location', r[0:], form.errors.as_data())

    def rollback(apps, schema_editor):
        Region = apps.get_model('locations', 'Region')
        Site = apps.get_model('locations', 'Site')
        MunicipalLocation = apps.get_model('locations', 'MunicipalLocation')
        StudyLocation = apps.get_model('locations', 'StudyLocation')
        StorageLocation = apps.get_model('locations', 'StorageLocation')

        for model in [StorageLocation, StudyLocation, MunicipalLocation, Site, Region]:
            model.objects.all().delete()

    dependencies = [
        ('locations', '0001_initial'),
        ('misc', '0002_DATA_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
