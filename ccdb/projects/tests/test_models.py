from datetime import datetime

from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import Project, Grant, GrantReport


def _project(name='project', code='p', iacuc_number='xyz', description='lorem ipsum',
             sort_order=1):
    return Project.objects.create(name=name, code=code, iacuc_number=iacuc_number,
                                  description=description, sort_order=sort_order)

def _grant(title='grant', code='g', description='lorem ipsum', sort_order=1):
    return Grant.objects.create(title=title, code=code, description=description,
                                sort_order=sort_order)


def _grant_report(title='grant report', grant=None, report_type='g',
                  description='lorem ipsum', due_date=datetime.now(), sort_order=1):
    if not grant:
        grant = _grant()
    return GrantReport.objects.create(grant=grant, title=title, report_type=report_type,
                                      description=description, due_date=due_date,
                                      sort_order=sort_order)


class ProjectTestCase(TestCase):
    def test_creation(self):
        p = _project()
        self.assertTrue(isinstance(p, Project))
        self.assertEqual(p.__str__(), p.name)

    def test_uniqueness(self):
        p1 = _project()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            p2 = _project()
        p3 = _project(name='abc')
        self.assertTrue(isinstance(p3, Project))


class GrantTestCase(TestCase):
    def test_creation(self):
        g = _grant()
        self.assertTrue(isinstance(g, Grant))
        self.assertEqual(g.__str__(), g.title)

    def test_uniqueness(self):
        g1 = _grant()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            g2 = _grant()
        g3 = _grant(title='abc')
        self.assertTrue(isinstance(g3, Grant))


class GrantReportTestCase(TestCase):
    def test_creation(self):
        g = _grant_report()
        self.assertTrue(isinstance(g, GrantReport))
        self.assertEqual(g.__str__(), g.title)

    def test_uniqueness(self):
        g1 = _grant_report()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            g2 = _grant_report()
        g3 = _grant_report(title='abc')
        self.assertTrue(isinstance(g3, GrantReport))
