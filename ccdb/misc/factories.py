import factory

from .models import MeasurementUnit, MeasurementType, Material, Color, Container


class MeasurementUnitFactory(factory.DjangoModelFactory):
    class Meta:
        model = MeasurementUnit

    name = factory.Sequence(lambda n: 'measurement_unit{}'.format(n))
    code = factory.Sequence(lambda n: 'mu{}'.format(n))
    unit_class = 'abc'
    description = 'lorem ipsum'
    sort_order = factory.Sequence(lambda n: n)


class MeasurementTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = MeasurementType

    name = factory.Sequence(lambda n: 'measurement_type{}'.format(n))
    code = factory.Sequence(lambda n: 'mt{}'.format(n))
    measurement_type_class = 'abc'
    description = 'lorem ipsum'
    default_measurement_unit = factory.SubFactory(MeasurementUnitFactory)
    sort_order = factory.Sequence(lambda n: n)


class MaterialFactory(factory.DjangoModelFactory):
    class Meta:
        model = Material

    name = factory.Sequence(lambda n: 'material{}'.format(n))
    code = factory.Sequence(lambda n: 'm{}'.format(n))
    material_class = 'abc'
    description = 'lorem ipsum'
    sort_order = factory.Sequence(lambda n: n)


class ColorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Color

    name = factory.Sequence(lambda n: 'color{}'.format(n))
    code = factory.Sequence(lambda n: 'c{}'.format(n))
    color_number = factory.Sequence(lambda n: float(n))
    sort_order = factory.Sequence(lambda n: n)


class ContainerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Container

    name = factory.Sequence(lambda n: 'container{}'.format(n))
    code = factory.Sequence(lambda n: 'c{}'.format(n))
    application = 'asdf'
    color = factory.SubFactory(ColorFactory)
    material = factory.SubFactory(MaterialFactory)
    volume = factory.Sequence(lambda n: float(n))
    measurement_unit = factory.SubFactory(MeasurementUnitFactory)
    sort_order = factory.Sequence(lambda n: n)
