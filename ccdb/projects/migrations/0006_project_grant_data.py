from django.db import migrations, models, transaction

from ccdb.utils.data_import import setup_sqlite


@transaction.atomic
def import_project_grant(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    Grant = apps.get_model('projects', 'Grant')
    c = setup_sqlite()
    if c:
        for r in c.execute('SELECT * FROM tbl_hash_project_grants;'):
            p = Project.objects.get(id=r[0])
            g = Grant.objects.get(id=r[1])
            p.grants.add(g)
            p.save()


def remove_project_grant(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_grant_projects'),
    ]

    operations = [
        migrations.RunPython(import_project_grant, remove_project_grant),
    ]
