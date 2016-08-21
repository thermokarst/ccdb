from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import Species, TrapSpecies, CollectionSpecies
from ..factories import (SpeciesFactory, TrapSpeciesFactory,
                         CollectionSpeciesFactory)


class SpeciesTestCase(TestCase):
    def test_creation(self):
        s = SpeciesFactory()
        self.assertTrue(isinstance(s, Species))
        self.assertEqual(s.__str__(), s.common_name)

    def test_uniqueness(self):
        s1 = SpeciesFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            SpeciesFactory(common_name=s1.common_name, species=s1.species)
        s3 = SpeciesFactory()
        self.assertTrue(isinstance(s3, Species))


class TrapSpeciesTestCase(TestCase):
    def test_creation(self):
        t = TrapSpeciesFactory()
        self.assertTrue(isinstance(t, TrapSpecies))
        label = "{} {}".format(t.collection_trap, t.species)
        self.assertEqual(t.__str__(), label)


class CollectionSpeciesTestCase(TestCase):
    def test_creation(self):
        c = CollectionSpeciesFactory()
        self.assertTrue(isinstance(c, CollectionSpecies))
        label = "{} {}".format(c.collection, c.species)
        self.assertEqual(c.__str__(), label)

    def test_uniqueness(self):
        c1 = CollectionSpeciesFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            CollectionSpeciesFactory(collection=c1.collection,
                                     species=c1.species)
        c3 = CollectionSpeciesFactory()
        self.assertTrue(isinstance(c3, CollectionSpecies))
