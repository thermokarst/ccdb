from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        ProcessType = apps.get_model('processing', 'ProcessType')
        Reagent = apps.get_model('processing', 'Reagent')
        Flaw = apps.get_model('processing', 'Flaw')
        Processing = apps.get_model('processing', 'Processing')

        for model in [Processing, Flaw, Reagent, ProcessType]:
            model.objects.all().delete()

        ProcessTypeForm = modelform_factory(ProcessType, fields='__all__')
        ReagentForm = modelform_factory(Reagent, fields='__all__')

        for r in c.execute('SELECT * FROM tbl_lu_process_types;'):
            form = ProcessTypeForm(dict(name=r[1], code=r[2],
                                    description=r[3],
                                    sort_order=int(r[4]) if r[4] else None))
            if form.is_valid():
                ProcessType.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('process type', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_reagents;'):
            form = ReagentForm(dict(name=r[1], code=r[2],
                                    reagent_class=r[3],
                                    sort_order=int(r[4]) if r[4] else None))
            if form.is_valid():
                Reagent.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('reagent', r[0:], form.errors.as_data())

    def rollback(apps, schema_editor):
        ProcessType = apps.get_model('processing', 'ProcessType')
        Reagent = apps.get_model('processing', 'Reagent')

        for model in [Reagent, ProcessType]:
            model.objects.all().delete()

    dependencies = [
        ('processing', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
