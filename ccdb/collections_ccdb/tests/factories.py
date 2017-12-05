from datetime import date, time

from factory import DjangoModelFactory, Sequence, SubFactory, LazyFunction
from factory.fuzzy import FuzzyText, FuzzyDate, FuzzyInteger
from factory.django import FileField

from ..models import (CollectionType, CollectionMethod, Flaw, ADFGPermit,
                      Collection, DatasheetAttachment, CollectionTrap)
from ccdb.projects.tests.factories import ProjectFactory
from ccdb.locations.tests.factories import (StudyLocationFactory,
                                            StorageLocationFactory)
from ccdb.processing.tests.factories import ProcessTypeFactory, ReagentFactory


class CollectionTypeFactory(DjangoModelFactory):
    class Meta:
        model = CollectionType

    name = Sequence(lambda n: 'collection_type{}'.format(n))
    code = Sequence(lambda n: 'ct{}'.format(n))
    sort_order = Sequence(lambda n: n)


class CollectionMethodFactory(DjangoModelFactory):
    class Meta:
        model = CollectionMethod

    name = Sequence(lambda n: 'collection_method{}'.format(n))
    code = Sequence(lambda n: 'cm{}'.format(n))
    collection_method_class = FuzzyText(length=50)
    sort_order = Sequence(lambda n: n)


class FlawFactory(DjangoModelFactory):
    class Meta:
        model = Flaw

    name = Sequence(lambda n: 'flaw{}'.format(n))
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)


class ADFGPermitFactory(DjangoModelFactory):
    class Meta:
        model = ADFGPermit

    name = Sequence(lambda n: 'adfg_permit{}'.format(n))
    sort_order = Sequence(lambda n: n)


class CollectionFactory(DjangoModelFactory):
    class Meta:
        model = Collection

    project = SubFactory(ProjectFactory)
    study_location = SubFactory(StudyLocationFactory)
    collection_type = SubFactory(CollectionTypeFactory)
    collection_method = SubFactory(CollectionMethodFactory)
    number_of_traps = FuzzyInteger(0)
    collection_start_date = FuzzyDate(date(2012, 1, 1))
    collection_start_time = None
    collection_end_date = FuzzyDate(date(2015, 1, 1))
    collection_end_time = None
    notes = FuzzyText(length=150)
    storage_location = SubFactory(StorageLocationFactory)
    specimen_state = FuzzyText(length=50)
    process_type = SubFactory(ProcessTypeFactory)
    reagent = SubFactory(ReagentFactory)
    adfg_permit = SubFactory(ADFGPermitFactory)
    collection_flaw = SubFactory(FlawFactory)


class DatasheetAttachmentFactory(DjangoModelFactory):
    class Meta:
        model = DatasheetAttachment

    collection = SubFactory(CollectionFactory)
    datasheet = FileField()


class CollectionTrapFactory(DjangoModelFactory):
    class Meta:
        model = CollectionTrap

    collection = SubFactory(CollectionFactory)
    number_of_traps = FuzzyInteger(0)
    date_opened = FuzzyDate(date(2012, 1, 1))
    time_opened = LazyFunction(time)
    date_closed = FuzzyDate(date(2015, 1, 1))
    time_closed = LazyFunction(time)
