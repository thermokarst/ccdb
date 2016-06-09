from factory import DjangoModelFactory, Sequence
from factory.fuzzy import FuzzyText, FuzzyChoice

from .models import Species


class SpeciesFactory(DjangoModelFactory):
    class Meta:
        model = Species

    common_name = Sequence(lambda n: 'species{}'.format(n))
    genus = FuzzyText(length=50)
    species = FuzzyText(length=50)
    parasite = FuzzyChoice(choices=[True, False])
    sort_order = Sequence(lambda n: n)
