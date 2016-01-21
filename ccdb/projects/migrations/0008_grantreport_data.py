from django.db import migrations, models, transaction

from ccdb.utils.data_import import setup_sqlite


@transaction.atomic
def import_grantreport(apps, schema_editor):
    GrantReport = apps.get_model('projects', 'GrantReport')
    Grant = apps.get_model('projects', 'Grant')
    c = setup_sqlite()
    if c:
        q = '''
               SELECT *, report_due_date AS "due_date [dtdt]"
               FROM tbl_lu_grant_reports;
            '''
        for r in c.execute(q):
            g = Grant.objects.get(id=r[0])
            gr = GrantReport(grant=g, title=r[1], report_type=r[2],
                description=r[3], due_date=r[8], submitted_date=r[5],
                attachment=r[6], sort_order=r[7])
            gr.save()


def remove_grantreport(apps, schema_editor):
    GrantReport = apps.get_model('projects', 'GrantReport')
    GrantReport.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_initial_grantreport'),
    ]

    operations = [
        migrations.RunPython(import_grantreport, remove_grantreport),
    ]
