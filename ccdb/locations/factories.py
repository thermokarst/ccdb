from factory import DjangoModelFactory, Sequence, SubFactory
from factory.fuzzy import FuzzyText, FuzzyChoice, FuzzyInteger

from .models import Region, Site, MunicipalLocation, StudyLocation, StorageLocation


class RegionFactory(DjangoModelFactory):
    class Meta:
        model = Region

    name = Sequence(lambda n: 'region{}'.format(n))
    code = Sequence(lambda n: 'r{}'.format(n))
    sort_order = Sequence(lambda n: n)


class SiteFactory(DjangoModelFactory):
    class Meta:
        model = Site

    region = SubFactory(RegionFactory)
    name = Sequence(lambda n: 'site{}'.format(n))
    code = Sequence(lambda n: 's{}'.format(n))
    description = FuzzyText(length=100)
    sort_order = Sequence(lambda n: n)


class MunicipalLocationFactory(DjangoModelFactory):
    class Meta:
        model = MunicipalLocation

    name = Sequence(lambda n: 'municipal_location{}'.format(n))
    code = Sequence(lambda n: 'ml{}'.format(n))
    municipal_location_type = FuzzyText(length=50)
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)


class StudyLocationFactory(DjangoModelFactory):
    class Meta:
        model = StudyLocation

    site = SubFactory(SiteFactory)
    name = Sequence(lambda n: 'study_location{}'.format(n))
    code = Sequence(lambda n: 'sl{}'.format(n))
    treatment_type = FuzzyText(length=100)
    municipal_location = SubFactory(MunicipalLocationFactory)
    collecting_location = FuzzyChoice([True, False])
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)


class StorageLocationFactory(DjangoModelFactory):
    class Meta:
        model = StorageLocation

    code = Sequence(lambda n: 'sl{}'.format(n))
    facility = FuzzyText(length=100)
    building = FuzzyText(length=100)
    room = FuzzyText(length=50)
    freezer = FuzzyText(length=50)
    temp_c = FuzzyInteger(-100, 100)
    description = FuzzyText(length=255)
    sort_order = Sequence(lambda n: n)
