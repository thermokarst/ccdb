from django.db import migrations, models, transaction

from ccdb.utils.data_import import setup_sqlite


@transaction.atomic
def import_grants(apps, schema_editor):
    Grant = apps.get_model('projects', 'Grant')
    c = setup_sqlite()
    if c:
        for r in c.execute('SELECT * FROM tbl_lu_grants;'):
            g = Grant(id=r[0], title=r[1], code=r[2],
                description=r[3], sort_order=r[4])
            g.save()


def remove_grants(apps, schema_editor):
    Grant = apps.get_model('projects', 'Grant')
    Grant.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_initial_grant'),
    ]

    operations = [
        migrations.RunPython(import_grants, remove_grants),
    ]
