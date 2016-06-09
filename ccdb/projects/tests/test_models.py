from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import Project, Grant, GrantReport
from ..factories import ProjectFactory, GrantFactory, GrantReportFactory


class ProjectTestCase(TestCase):
    def test_creation(self):
        p = ProjectFactory()
        self.assertTrue(isinstance(p, Project))
        self.assertEqual(p.__str__(), p.name)

    def test_uniqueness(self):
        p1 = ProjectFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            ProjectFactory(name=p1.name, code=p1.code)
        p3 = ProjectFactory()
        self.assertTrue(isinstance(p3, Project))


class GrantTestCase(TestCase):
    def test_creation(self):
        g = GrantFactory()
        self.assertTrue(isinstance(g, Grant))
        self.assertEqual(g.__str__(), g.title)

    def test_uniqueness(self):
        g1 = GrantFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            GrantFactory(title=g1.title, code=g1.code)
        g3 = GrantFactory()
        self.assertTrue(isinstance(g3, Grant))


class GrantReportTestCase(TestCase):
    def test_creation(self):
        g = GrantReportFactory()
        self.assertTrue(isinstance(g, GrantReport))
        self.assertEqual(g.__str__(), g.title)

    def test_uniqueness(self):
        g1 = GrantReportFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            GrantReportFactory(title=g1.title, grant=g1.grant)
        g3 = GrantReportFactory()
        self.assertTrue(isinstance(g3, GrantReport))
