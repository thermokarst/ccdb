from datetime import date, time

from factory import DjangoModelFactory, Sequence, SubFactory, \
    LazyFunction, post_generation
from factory.fuzzy import FuzzyText, FuzzyDate, FuzzyInteger, FuzzyFloat
from factory.django import FileField

from .models import Flaw, Experiment, ProtocolAttachment, TreatmentType, \
    Treatment, TreatmentReplicate, AliveDeadCount
from ..misc.factories import ContainerFactory
from ..locations.factories import StudyLocationFactory
from ..species.factories import SpeciesFactory


class FlawFactory(DjangoModelFactory):
    class Meta:
        model = Flaw

    name = Sequence(lambda n: 'flaw{}'.format(n))
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)


class ExperimentFactory(DjangoModelFactory):
    class Meta:
        model = Experiment

    name = Sequence(lambda n: 'experiment{}'.format(n))
    code = Sequence(lambda n: 'e{}'.format(n))
    description = FuzzyText(length=255)
    flaw = SubFactory(FlawFactory)
    sort_order = Sequence(lambda n: n)

    @post_generation
    def collections(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for collection in extracted:
                self.groups.add(collection)


class ProtocolAttachmentFactory(DjangoModelFactory):
    class Meta:
        model = ProtocolAttachment

    experiment = SubFactory(ExperimentFactory)
    protocol = FileField()


class TreatmentTypeFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentType

    experiment = SubFactory(ExperimentFactory)
    name = Sequence(lambda n: 'treatment_type{}'.format(n))
    code = Sequence(lambda n: 'tt{}'.format(n))
    treatment_type = FuzzyText(length=50)
    placement = FuzzyText(length=25)
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)


class TreatmentFactory(DjangoModelFactory):
    class Meta:
        model = Treatment

    treatment_type = SubFactory(TreatmentTypeFactory)
    container = SubFactory(ContainerFactory)
    study_location = SubFactory(StudyLocationFactory)
    species = SubFactory(SpeciesFactory)
    sex = FuzzyText(length=25)
    flaw = SubFactory(FlawFactory)


class TreatmentReplicateFactory(DjangoModelFactory):
    class Meta:
        model = TreatmentReplicate

    treatment = SubFactory(TreatmentFactory)
    name = Sequence(lambda n: 'treatment_replicate{}'.format(n))
    setup_date = FuzzyDate(date(2012, 1, 1))
    setup_time = LazyFunction(time)
    setup_sample_size = FuzzyInteger(0)
    mass_g = FuzzyFloat(0.0)
    flaw = SubFactory(FlawFactory)


class AliveDeadCountFactory(DjangoModelFactory):
    class Meta:
        model = AliveDeadCount

    treatment_replicate = SubFactory(TreatmentReplicateFactory)
    status_date = FuzzyDate(date(2012, 1, 1))
    status_time = LazyFunction(time)
    count_alive = FuzzyInteger(0)
    count_dead = FuzzyInteger(0)
    flaw = SubFactory(FlawFactory)
