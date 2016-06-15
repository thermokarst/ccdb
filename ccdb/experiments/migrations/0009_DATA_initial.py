from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        Flaw = apps.get_model('experiments', 'Flaw')
        Experiment = apps.get_model('experiments', 'Experiment')
        TreatmentType = apps.get_model('experiments', 'TreatmentType')
        Treatment = apps.get_model('experiments', 'Treatment')
        TreatmentReplicate = apps.get_model('experiments', 'TreatmentReplicate')
        AliveDeadCount = apps.get_model('experiments', 'AliveDeadCount')

        for model in [AliveDeadCount, TreatmentReplicate, Treatment, TreatmentType,
                      Experiment, Flaw]:
            model.objects.all().delete()

        ExperimentForm = modelform_factory(Experiment, exclude=('collections',))
        TreatmentTypeForm = modelform_factory(TreatmentType, fields='__all__')
        TreatmentForm = modelform_factory(Treatment, fields='__all__')
        TreatmentReplicateForm = modelform_factory(TreatmentReplicate, fields='__all__')
        AliveDeadCountForm = modelform_factory(AliveDeadCount, fields='__all__')

        for r in c.execute('SELECT * FROM tbl_lu_experiments;'):
            form = ExperimentForm(dict(name=r[1], code=r[2], description=r[3],
                                       sort_order=int(r[4]) if r[4] else None))
            if form.is_valid():
                Experiment.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('experiment', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_treatment_types;'):
            form = TreatmentTypeForm(dict(experiment=r[0], name=r[2], code=r[3],
                                          treatment_type=r[4], placement=r[5],
                                          description=r[6]))
            if form.is_valid():
                TreatmentType.objects.create(id=r[1], **form.cleaned_data)
            else:
                print('treatment type', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_treatments;'):
            form = TreatmentForm(dict(treatment_type=r[1], container=r[2],
                                      study_location=r[3], species=r[4], sex=r[5]))
            if form.is_valid():
                Treatment.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('treatment', r[0:], form.errors.as_data())

        for r in c.execute('''
                SELECT *, setup_date AS "setup_date [dtdt]"
                FROM tbl_treatment_replicates tr
                LEFT OUTER JOIN tbl_lu_record_flaws f ON f.flawid=tr.flawid;
                '''):
            flaw = None
            if r[7]:
                flaw = Flaw.objects.create(name=r[10]).pk
            form = TreatmentReplicateForm(dict(treatment=r[0], name=r[2],
                                               setup_date=r[13],
                                               setup_sample_size=r[5], mass_g=r[6],
                                               flaw=flaw))
            if form.is_valid():
                TreatmentReplicate.objects.create(id=r[1], **form.cleaned_data)
            else:
                print('treatment replicate', r[0:], form.errors.as_data())

        for r in c.execute('''
                SELECT *,
                    status_date AS "status_date [dtdt]",
                    status_time AS "status_time [dtdt]"
                FROM tbl_alive_dead_counts adc
                LEFT OUTER JOIN tbl_lu_record_flaws f ON f.flawid=adc.flawid;
                '''):
            flaw = None
            if r[6]:
                flaw = Flaw.objects.create(name=r[9]).pk
            form = AliveDeadCountForm(dict(treatment_replicate=r[0],
                                           status_date=r[12],
                                           status_time=r[13].time() if r[13] else None,
                                           count_alive=r[4], count_dead=r[5],
                                           flaw=flaw))
            if form.is_valid():
                AliveDeadCount.objects.create(id=r[1], **form.cleaned_data)
            else:
                print('alive-dead count', r[0:], form.errors.as_data())

    def rollback(apps, schema_editor):
        Flaw = apps.get_model('experiments', 'Flaw')
        Experiment = apps.get_model('experiments', 'Experiment')
        TreatmentType = apps.get_model('experiments', 'TreatmentType')
        Treatment = apps.get_model('experiments', 'Treatment')
        TreatmentReplicate = apps.get_model('experiments', 'TreatmentReplicate')
        AliveDeadCount = apps.get_model('experiments', 'AliveDeadCount')

        for model in [AliveDeadCount, TreatmentReplicate, Treatment, TreatmentType,
                      Experiment, Flaw]:
            model.objects.all().delete()

    dependencies = [
        ('experiments', '0008_treatment_display_name'),
        ('collections_ccdb', '0005_DATA_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
