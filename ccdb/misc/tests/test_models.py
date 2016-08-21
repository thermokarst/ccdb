from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import (MeasurementUnit, MeasurementType, Material, Color,
                      Container)
from .factories import (MeasurementUnitFactory, MeasurementTypeFactory,
                        MaterialFactory, ColorFactory, ContainerFactory)


class MeasurementUnitTestCase(TestCase):
    def test_creation(self):
        m = MeasurementUnitFactory()
        self.assertTrue(isinstance(m, MeasurementUnit))
        self.assertEqual(m.__str__(), m.code)

    def test_uniqueness(self):
        m1 = MeasurementUnitFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            MeasurementUnitFactory(name=m1.name, code=m1.code)
        m3 = MeasurementUnitFactory()
        self.assertTrue(isinstance(m3, MeasurementUnit))


class MeasurementTypeTestCase(TestCase):
    def test_creation(self):
        m = MeasurementTypeFactory()
        self.assertTrue(isinstance(m, MeasurementType))
        self.assertEqual(m.__str__(), m.name)

    def test_uniqueness(self):
        m1 = MeasurementTypeFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            MeasurementTypeFactory(name=m1.name, code=m1.code,
                                   measurement_type_class=m1.measurement_type_class)
        m3 = MeasurementTypeFactory()
        self.assertTrue(isinstance(m3, MeasurementType))


class MaterialTestCase(TestCase):
    def test_creation(self):
        m = MaterialFactory()
        self.assertTrue(isinstance(m, Material))
        self.assertEqual(m.__str__(), m.name)

    def test_uniqueness(self):
        m1 = MaterialFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            MaterialFactory(name=m1.name, code=m1.code)
        m3 = MaterialFactory()
        self.assertTrue(isinstance(m3, Material))


class ColorTestCase(TestCase):
    def test_creation(self):
        c = ColorFactory()
        self.assertTrue(isinstance(c, Color))
        self.assertEqual(c.__str__(), c.name)

    def test_uniqueness(self):
        c1 = ColorFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ColorFactory(name=c1.name, code=c1.code, color_number=c1.color_number)
        c3 = ColorFactory()
        self.assertTrue(isinstance(c3, Color))


class ContainerTestCase(TestCase):
    def test_creation(self):
        c = ContainerFactory()
        self.assertTrue(isinstance(c, Container))
        self.assertEqual(c.__str__(), c.name)

    def test_uniqueness(self):
        c1 = ContainerFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ContainerFactory(name=c1.name, code=c1.code, color=c1.color,
                             material=c1.material, volume=c1.volume)
        c3 = ContainerFactory()
        self.assertTrue(isinstance(c3, Container))
