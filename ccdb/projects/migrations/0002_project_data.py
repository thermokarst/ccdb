from django.db import migrations, models, transaction

from ccdb.utils.data_import import setup_sqlite


@transaction.atomic
def import_projects(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    c = setup_sqlite()
    if c:
        for r in c.execute('SELECT * FROM tbl_lu_projects;'):
            p = Project(id=r[0], name=r[1], code=r[2], iacuc_number=r[3],
                description=r[4], sort_order=r[5])
            p.save()


def remove_projects(apps, schema_editor):
    print("removing projects...")
    Project = apps.get_model("projects", "Project")
    Project.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial_project'),
    ]

    operations = [
        migrations.RunPython(import_projects, remove_projects),
    ]
