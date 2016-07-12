from django.db import migrations, models


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        Collection = apps.get_model('collections_ccdb', 'Collection')

        for c in Collection.objects.all():
            d = "{}_{}_{}_{}".format(c.project.name,
                                     c.collection_end_date,
                                     c.study_location.code,
                                     c.collection_type.name)
            c.display_name = d
            c.save()

    dependencies = [
        ('collections_ccdb', '0002_DATA_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, migrations.RunPython.noop)
    ]
