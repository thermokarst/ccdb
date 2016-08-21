from factory import DjangoModelFactory, Sequence, SubFactory
from factory.fuzzy import FuzzyText, FuzzyChoice, FuzzyInteger

from ..models import Species, TrapSpecies, CollectionSpecies
from ccdb.collections_ccdb.tests.factories import (CollectionFactory,
                                                   CollectionTrapFactory)


class SpeciesFactory(DjangoModelFactory):
    class Meta:
        model = Species

    common_name = Sequence(lambda n: 'species{}'.format(n))
    genus = FuzzyText(length=50)
    species = FuzzyText(length=50)
    parasite = FuzzyChoice(choices=[True, False])
    sort_order = Sequence(lambda n: n)


class TrapSpeciesFactory(DjangoModelFactory):
    class Meta:
        model = TrapSpecies

    collection_trap = SubFactory(CollectionTrapFactory)
    species = SubFactory(SpeciesFactory)
    sex = FuzzyText(length=25)
    count = FuzzyInteger(0)
    count_estimated = FuzzyChoice(choices=[True, False])


class CollectionSpeciesFactory(DjangoModelFactory):
    class Meta:
        model = CollectionSpecies

    collection = SubFactory(CollectionFactory)
    species = SubFactory(SpeciesFactory)
    sex = FuzzyText(length=25)
    count = FuzzyInteger(0)
    count_estimated = FuzzyChoice(choices=[True, False])
