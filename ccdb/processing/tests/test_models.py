from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import ProcessType, Reagent, Flaw, Processing
from .factories import (ProcessTypeFactory, ReagentFactory, FlawFactory,
                        ProcessingFactory)


class ProcessTypeTestCase(TestCase):
    def test_creation(self):
        p = ProcessTypeFactory()
        self.assertTrue(isinstance(p, ProcessType))
        self.assertEqual(p.__str__(), p.name)

    def test_uniqueness(self):
        p1 = ProcessTypeFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ProcessTypeFactory(name=p1.name, code=p1.code)
        p3 = ProcessTypeFactory()
        self.assertTrue(isinstance(p3, ProcessType))


class ReagentTestCase(TestCase):
    def test_creation(self):
        r = ReagentFactory()
        self.assertTrue(isinstance(r, Reagent))
        self.assertEqual(r.__str__(), r.name)

    def test_uniqueness(self):
        r1 = ReagentFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ReagentFactory(name=r1.name, code=r1.code)
        r3 = ReagentFactory()
        self.assertTrue(isinstance(r3, Reagent))


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


class ProcessingTestCase(TestCase):
    def test_creation(self):
        p = ProcessingFactory()
        self.assertTrue(isinstance(p, Processing))
        name = "{} {} {}".format(p.process_date, p.process_type,
                                 p.container_label)
        self.assertEqual(p.__str__(), name)

    def test_uniqueness(self):
        p1 = ProcessingFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ProcessingFactory(process_type=p1.process_type,
                              container=p1.container,
                              container_label=p1.container_label,
                              process_date=p1.process_date,
                              process_time=p1.process_time, reagent=p1.reagent)
        p3 = ProcessingFactory()
        self.assertTrue(isinstance(p3, Processing))
