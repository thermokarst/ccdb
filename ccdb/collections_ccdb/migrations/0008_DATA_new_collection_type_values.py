from django.db import migrations
from django.forms import modelform_factory


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        CollectionType = apps.get_model('collections_ccdb', 'CollectionType')
        CollectionTypeForm = modelform_factory(CollectionType,
                                               fields=('name',))
        for ct in ['Juvenile', 'Mixed Ages']:
            form = CollectionTypeForm(dict(name=ct))
            if form.is_valid():
                CollectionType.objects.create(**form.cleaned_data)
            else:
                print('collection type', form.errors.as_data())

    dependencies = [
        ('collections_ccdb', '0007_collection_measurements'),
    ]

    operations = [
        migrations.RunPython(migrate),
    ]
