from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import (CollectionType, CollectionMethod, Flaw, ADFGPermit,
                      Collection, DatasheetAttachment, CollectionTrap)
from .factories import (CollectionTypeFactory, CollectionMethodFactory,
                        FlawFactory, ADFGPermitFactory, CollectionFactory,
                        DatasheetAttachmentFactory, CollectionTrapFactory)


class CollectionTypeTestCase(TestCase):
    def test_creation(self):
        c = CollectionTypeFactory()
        self.assertTrue(isinstance(c, CollectionType))
        self.assertEqual(c.__str__(), c.name)

    def test_uniqueness(self):
        c1 = CollectionTypeFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            CollectionTypeFactory(name=c1.name, code=c1.code)
        c3 = CollectionTypeFactory()
        self.assertTrue(isinstance(c3, CollectionType))


class CollectionMethodTestCase(TestCase):
    def test_creation(self):
        c = CollectionMethodFactory()
        self.assertTrue(isinstance(c, CollectionMethod))
        self.assertEqual(c.__str__(), c.name)

    def test_uniqueness(self):
        c1 = CollectionMethodFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            CollectionMethodFactory(name=c1.name, code=c1.code)
        c3 = CollectionMethodFactory()
        self.assertTrue(isinstance(c3, CollectionMethod))


class FlawTestCase(TestCase):
    def test_creation(self):
        f = FlawFactory()
        self.assertTrue(isinstance(f, Flaw))
        self.assertEqual(f.__str__(), f.name)

    def test_uniqueness(self):
        f1 = FlawFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            FlawFactory(name=f1.name)
        f3 = FlawFactory()
        self.assertTrue(isinstance(f3, Flaw))


class ADFGPermitTestCase(TestCase):
    def test_creation(self):
        a = ADFGPermitFactory()
        self.assertTrue(isinstance(a, ADFGPermit))
        self.assertEqual(a.__str__(), a.name)

    def test_uniqueness(self):
        a1 = ADFGPermitFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ADFGPermitFactory(name=a1.name)
        a3 = ADFGPermitFactory()
        self.assertTrue(isinstance(a3, ADFGPermit))


class CollectionTestCase(TestCase):
    def test_creation(self):
        c = CollectionFactory()
        self.assertTrue(isinstance(c, Collection))
        self.assertEqual(c.__str__(), c.display_name)

    def test_uniqueness(self):
        c1 = CollectionFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            CollectionFactory(project=c1.project, study_location=c1.study_location,
                              collection_type=c1.collection_type,
                              collection_start_date=c1.collection_start_date,
                              collection_end_date=c1.collection_end_date,
                              collection_method=c1.collection_method)
        c3 = CollectionFactory()
        self.assertTrue(isinstance(c3, Collection))


class DatasheetAttachmentTestCase(TestCase):
    def test_creation(self):
        d = DatasheetAttachmentFactory()
        self.assertTrue(isinstance(d, DatasheetAttachment))


class CollectionTrapTestCase(TestCase):
    def test_creation(self):
        c = CollectionTrapFactory()
        self.assertTrue(isinstance(c, CollectionTrap))
        name = "{} # Traps: {} {} {}".format(c.collection, c.number_of_traps,
                                             c.date_opened, c.date_closed)
        self.assertEqual(c.__str__(), name)

    def test_uniqueness(self):
        c1 = CollectionTrapFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            CollectionTrapFactory(collection=c1.collection, date_opened=c1.date_opened,
                                  time_opened=c1.time_opened, date_closed=c1.date_closed,
                                  time_closed=c1.time_closed)
        c3 = CollectionTrapFactory()
        self.assertTrue(isinstance(c3, CollectionTrap))
