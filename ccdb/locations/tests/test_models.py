from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import (Region, Site, MunicipalLocation, StudyLocation,
                      StorageLocation)
from .factories import (RegionFactory, SiteFactory, MunicipalLocationFactory,
                        StudyLocationFactory, StorageLocationFactory)


class RegionTestCase(TestCase):
    def test_creation(self):
        r = RegionFactory()
        self.assertTrue(isinstance(r, Region))
        self.assertEqual(r.__str__(), r.name)

    def test_uniqueness(self):
        r1 = RegionFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            RegionFactory(name=r1.name, code=r1.code)
        r3 = RegionFactory()
        self.assertTrue(isinstance(r3, Region))


class SiteTestCase(TestCase):
    def test_creation(self):
        s = SiteFactory()
        self.assertTrue(isinstance(s, Site))
        self.assertEqual(s.__str__(), s.name)

    def test_uniqueness(self):
        s1 = SiteFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            SiteFactory(region=s1.region, name=s1.name, code=s1.code)
        s3 = SiteFactory()
        self.assertTrue(isinstance(s3, Site))


class MunicipalLocationTestCase(TestCase):
    def test_creation(self):
        m = MunicipalLocationFactory()
        self.assertTrue(isinstance(m, MunicipalLocation))
        self.assertEqual(m.__str__(), m.name)

    def test_uniqueness(self):
        m1 = MunicipalLocationFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            MunicipalLocationFactory(name=m1.name, code=m1.code)
        m3 = MunicipalLocationFactory()
        self.assertTrue(isinstance(m3, MunicipalLocation))


class StudyLocationTestCase(TestCase):
    def test_creation(self):
        s = StudyLocationFactory()
        self.assertTrue(isinstance(s, StudyLocation))
        self.assertEqual(s.__str__(), s.code)

    def test_uniqueness(self):
        s1 = StudyLocationFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            StudyLocationFactory(site=s1.site, name=s1.name)
        s3 = StudyLocationFactory()
        self.assertTrue(isinstance(s3, StudyLocation))


class StorageLocationTestCase(TestCase):
    def test_creation(self):
        s = StorageLocationFactory()
        self.assertTrue(isinstance(s, StorageLocation))
        self.assertEqual(s.__str__(), s.code)

    def test_uniqueness(self):
        s1 = StorageLocationFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            StorageLocationFactory(code=s1.code, facility=s1.facility,
                                   building=s1.building, room=s1.room,
                                   freezer=s1.freezer, temp_c=s1.temp_c)
        s3 = StorageLocationFactory()
        self.assertTrue(isinstance(s3, StorageLocation))
