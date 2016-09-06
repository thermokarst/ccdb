from collections import namedtuple

from django.db import migrations


Section = namedtuple('Section', ['name', 'package', 'entries'])


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        AdminSection = apps.get_model('utils', 'AdminSection')
        AdminEntry = apps.get_model('utils', 'AdminEntry')

        # Clean up any old stuff
        for model in [AdminEntry, AdminSection]:
            model.objects.all().delete()

        data = [
            Section('Collections', 'collections_ccdb', [
                'collectiontype', 'collectionmethod', 'flaw', 'adfgpermit',
                'datasheetattachment', 'collectiontrap', 'collection'
            ]),
            Section('Experiments', 'experiments', [
                'flaw', 'experiment', 'protocolattachment', 'treatmenttype',
                'treatment', 'treatmentreplicate', 'alivedeadcount'
            ]),
            Section('Locations', 'locations', [
                'region', 'site', 'municipallocation', 'studylocation',
                'storagelocation'
            ]),
            Section('Misc.', 'misc', [
                'measurementunit', 'measurementtype', 'container', 'material',
                'color'
            ]),
            Section('Processing', 'processing', [
                'processtype', 'reagent', 'flaw'
            ]),
            Section('Projects', 'projects', [
                'project', 'grant', 'grantreport'
            ]),
            Section('Species', 'species', [
                'species', 'trapspecies', 'collectionspecies'
            ]),
            Section('Users', 'users', [
                'user'
            ]),
            Section('Utils', 'utils', [
                'adminsection', 'adminentry'
            ]),
        ]

        for i, adminsection in enumerate(data):
            section = AdminSection.objects.create(name=adminsection.name,
                                                  sort=i)
            for j, entry in enumerate(adminsection.entries):
                AdminEntry.objects.create(package=adminsection.package,
                                          model=entry, section=section, sort=j)

    def rollback(apps, schema_editor):
        AdminSection = apps.get_model('utils', 'AdminSection')
        AdminEntry = apps.get_model('utils', 'AdminEntry')

        for model in [AdminEntry, AdminSection]:
            model.objects.all().delete()

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
