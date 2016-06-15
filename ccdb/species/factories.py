from factory import DjangoModelFactory, Sequence, SubFactory
from factory.fuzzy import FuzzyText, FuzzyChoice, FuzzyInteger

from .models import Species, CollectionSpecies
from ..collections_ccdb.factories import CollectionFactory


class SpeciesFactory(DjangoModelFactory):
    class Meta:
        model = Species

    common_name = Sequence(lambda n: 'species{}'.format(n))
    genus = FuzzyText(length=50)
    species = FuzzyText(length=50)
    parasite = FuzzyChoice(choices=[True, False])
    sort_order = Sequence(lambda n: n)


class CollectionSpeciesFactory(DjangoModelFactory):
    class Meta:
        model = CollectionSpecies

    collection = SubFactory(CollectionFactory)
    species = SubFactory(SpeciesFactory)
    sex = FuzzyText(length=25)
    count = FuzzyInteger(0)
    count_estimated = FuzzyChoice(choices=[True, False])
