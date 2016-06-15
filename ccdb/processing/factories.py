from datetime import datetime, date

from factory import DjangoModelFactory, Sequence, SubFactory, LazyFunction
from factory.fuzzy import FuzzyText, FuzzyDate, FuzzyFloat, FuzzyInteger

from .models import ProcessType, Reagent, Flaw, Processing
from ..misc.factories import ContainerFactory, MeasurementUnitFactory


class ProcessTypeFactory(DjangoModelFactory):
    class Meta:
        model = ProcessType

    name = Sequence(lambda n: 'process_type{}'.format(n))
    code = Sequence(lambda n: 'pt{}'.format(n))
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)


class ReagentFactory(DjangoModelFactory):
    class Meta:
        model = Reagent

    name = Sequence(lambda n: 'reagent{}'.format(n))
    code = Sequence(lambda n: 'r{}'.format(n))
    reagent_class = FuzzyText(length=50)
    sort_order = Sequence(lambda n: n)


class FlawFactory(DjangoModelFactory):
    class Meta:
        model = Flaw

    name = Sequence(lambda n: 'flaw{}'.format(n))
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)


class ProcessingFactory(DjangoModelFactory):
    class Meta:
        model = Processing

    process_type = SubFactory(ProcessTypeFactory)
    container = SubFactory(ContainerFactory)
    container_label = FuzzyText(length=50)
    process_date = FuzzyDate(date(2012, 1, 1))
    process_time = LazyFunction(datetime.now().time)
    reagent = SubFactory(ReagentFactory)
    reagent_volume = FuzzyFloat(0.0)
    measurement_unit = SubFactory(MeasurementUnitFactory)
    minutes_in_reagent = FuzzyInteger(0)
    flaw = SubFactory(FlawFactory)
