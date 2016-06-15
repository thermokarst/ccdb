from django.db import migrations
from django.forms import modelform_factory

from ccdb.utils.data import get_data_sources


class Migration(migrations.Migration):
    def migrate(apps, schema_editor):
        sources = get_data_sources()
        if not sources:
            return

        c = sources['db0']

        MeasurementUnit = apps.get_model('misc', 'MeasurementUnit')
        MeasurementType = apps.get_model('misc', 'MeasurementType')
        Material = apps.get_model('misc', 'Material')
        Color = apps.get_model('misc', 'Color')
        Container = apps.get_model('misc', 'Container')

        for model in [Container, MeasurementType, MeasurementUnit, Material, Color]:
            model.objects.all().delete()

        MUnitForm = modelform_factory(MeasurementUnit, fields=('name', 'code',
                                                               'unit_class',
                                                               'description',
                                                               'sort_order'))
        MTypeForm = modelform_factory(MeasurementType, fields=('name', 'code',
                                                               'measurement_type_class',
                                                               'description',
                                                               'default_measurement_unit',
                                                               'sort_order'))
        MaterialForm = modelform_factory(Material, fields=('name', 'code',
                                                           'material_class',
                                                           'description',
                                                           'sort_order'))
        ColorForm = modelform_factory(Color, fields=('name', 'code',
                                                     'color_number',
                                                     'sort_order'))
        ContainerForm = modelform_factory(Container, fields=('name', 'code',
                                                             'application',
                                                             'color', 'material',
                                                             'volume',
                                                             'measurement_unit',
                                                             'sort_order'))

        for r in c.execute('SELECT * FROM tbl_lu_measurement_units;'):
            form = MUnitForm(dict(name=r[1], code=r[2],
                                  unit_class=r[3], description=r[4],
                                  sort_order=int(r[5]) if r[5] else None))
            if form.is_valid():
                MeasurementUnit.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('measurement unit', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_measurement_types;'):
            form = MTypeForm(dict(name=r[1], code=r[2],
                                  measurement_type_class=r[3], description=r[4],
                                  default_measurement_unit=r[5],
                                  sort_order=int(r[6]) if r[6] else None))
            if form.is_valid():
                MeasurementType.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('measurement type', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_materials;'):
            form = MaterialForm(dict(name=r[1], code=r[2],
                                     material_class=r[3], description=r[4],
                                     sort_order=int(r[5]) if r[5] else None))
            if form.is_valid():
                Material.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('material', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_colors;'):
            form = ColorForm(dict(name=r[1], code=r[2],
                                  color_number=float(r[3]) if r[3] else None,
                                  sort_order=int(r[4]) if r[4] else None))
            if form.is_valid():
                Color.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('color', r[0:], form.errors.as_data())

        for r in c.execute('SELECT * FROM tbl_lu_containers;'):
            form = ContainerForm(dict(name=r[1], code=r[2],
                                      application=r[3], color=r[4], material=r[5],
                                      volume=float(r[6]) if r[6] else None,
                                      measurement_unit=r[7],
                                      sort_order=int(r[8]) if r[8] else None))
            if form.is_valid():
                Container.objects.create(id=r[0], **form.cleaned_data)
            else:
                print('container', r[0:], form.errors.as_data())

    def rollback(apps, schema_editor):
        MeasurementUnit = apps.get_model('misc', 'MeasurementUnit')
        MeasurementType = apps.get_model('misc', 'MeasurementType')
        Material = apps.get_model('misc', 'Material')
        Color = apps.get_model('misc', 'Color')
        Container = apps.get_model('misc', 'Container')

        for model in [Container, MeasurementType, MeasurementUnit, Material, Color]:
            model.objects.all().delete()

    dependencies = [
        ('misc', '0001_initial'),
        ('projects', '0002_DATA_initial'),
    ]

    operations = [
        migrations.RunPython(migrate, rollback),
    ]
