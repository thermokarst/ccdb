from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import Species
from ..factories import SpeciesFactory


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
