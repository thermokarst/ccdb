from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        Project = apps.get_model('projects', 'Project')
        Grant = apps.get_model('projects', 'Grant')
        GrantReport = apps.get_model('projects', 'GrantReport')

        Project.objects.all().delete()
        Grant.objects.all().delete()
        GrantReport.objects.all().delete()

        ProjectForm = modelform_factory(Project, fields=('name', 'code',
                                                         'iacuc_number',
                                                         'description',
                                                         'sort_order'))
        GrantForm = modelform_factory(Grant, fields=('title', 'code',
                                                     'description', 'sort_order'))
        GrantReportForm = modelform_factory(GrantReport, fields=('grant', 'title',
                                                                 'report_type',
                                                                 'description',
                                                                 'due_date',
                                                                 'submitted_date',
                                                                 'sort_order'))

        for r in c.execute('SELECT * FROM tbl_lu_projects;'):
            form = ProjectForm(dict(name=r[1], code=r[2],
                                    iacuc_number=r[3], description=r[4],
                                    sort_order=int(r[5])))
            if form.is_valid():
                Project.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('project', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_grants;'):
            form = GrantForm(dict(title=r[1], code=r[2], description=r[3], sort_order=r[4]))
            if form.is_valid():
                Grant.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('grant', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_hash_project_grants;'):
            p = Project.objects.get(id=r[0])
            g = Grant.objects.get(id=r[1])
            p.grants.add(g)
            p.save()

        for r in c.execute('SELECT *, report_due_date AS "due_date [dtdt]" FROM tbl_lu_grant_reports;'):
            form = GrantReportForm(dict(grant=r[0], title=r[1], report_type=r[2],
                                        description=r[3], due_date=r[8],
                                        submitted_date=r[5], sort_order=r[7]))
            if form.is_valid():
                form.save()  # No PK field in Andre's file
            else:
                print('grant report', r[0:], form.errors.as_data())


    def rollback(apps, schema_editor):
        Project = apps.get_model('projects', 'Project')
        Grant = apps.get_model('projects', 'Grant')
        GrantReport = apps.get_model('projects', 'GrantReport')

        for model in [Project, Grant, GrantReport]:
            model.objects.all().delete()

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
