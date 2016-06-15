from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import Flaw, Experiment, ProtocolAttachment, TreatmentType, \
    Treatment, TreatmentReplicate, AliveDeadCount
from ..factories import FlawFactory, ExperimentFactory, ProtocolAttachmentFactory, \
    TreatmentTypeFactory, TreatmentFactory, TreatmentReplicateFactory, \
    AliveDeadCountFactory


class FlawTestCase(TestCase):
    def test_creation(self):
        f = FlawFactory()
        self.assertTrue(isinstance(f, Flaw))
        self.assertEqual(f.__str__(), f.name)


class ExperimentTestCase(TestCase):
    def test_creation(self):
        e = ExperimentFactory()
        self.assertTrue(isinstance(e, Experiment))
        self.assertEqual(e.__str__(), e.name)

    def test_uniqueness(self):
        e1 = ExperimentFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ExperimentFactory(name=e1.name, code=e1.code)
        e3 = ExperimentFactory()
        self.assertTrue(isinstance(e3, Experiment))


class ProtocolAttachmentTestCase(TestCase):
    def test_creation(self):
        p = ProtocolAttachmentFactory()
        self.assertTrue(isinstance(p, ProtocolAttachment))
        self.assertEqual(p.__str__(), p.protocol)


class TreatmentTypeTestCase(TestCase):
    def test_creation(self):
        t = TreatmentTypeFactory()
        self.assertTrue(isinstance(t, TreatmentType))
        label = "{} {} {} {}".format(t.experiment, t.name, t.treatment_type,
                                     t.placement)
        self.assertEqual(t.__str__(), label)

    def test_uniqueness(self):
        t1 = TreatmentTypeFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            TreatmentTypeFactory(name=t1.name, experiment=t1.experiment)
        t3 = TreatmentTypeFactory()
        self.assertTrue(isinstance(t3, TreatmentType))


class TreatmentTestCase(TestCase):
    def test_creation(self):
        t = TreatmentFactory()
        self.assertTrue(isinstance(t, Treatment))
        label = "{}_{}_{}_{}".format(t.treatment_type, t.study_location,
                                     t.species, t.sex)
        self.assertEqual(t.__str__(), label)


class TreatmentReplicateTestCase(TestCase):
    def test_creation(self):
        t = TreatmentReplicateFactory()
        self.assertTrue(isinstance(t, TreatmentReplicate))
        label = "{}_{}_{}_{}".format(t.treatment, t.setup_date,
                                     t.name, t.setup_sample_size)
        self.assertEqual(t.__str__(), label)

    def test_uniqueness(self):
        t1 = TreatmentReplicateFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            TreatmentReplicateFactory(treatment=t1.treatment, name=t1.name,
                                      setup_date=t1.setup_date,
                                      setup_time=t1.setup_time)
        t3 = TreatmentReplicateFactory()
        self.assertTrue(isinstance(t3, TreatmentReplicate))


class AliveDeadCountTestCase(TestCase):
    def test_creation(self):
        a = AliveDeadCountFactory()
        self.assertTrue(isinstance(a, AliveDeadCount))
        label = "{}".format(a.status_date)
        self.assertEqual(a.__str__(), label)
