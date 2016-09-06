from django.test import TestCase
from django.test.client import RequestFactory

from ..models import AdminSection, AdminEntry
from .factories import AdminSectionFactory, AdminEntryFactory


class AdminSectionTestCase(TestCase):
    def test_creation(self):
        a = AdminSectionFactory()
        self.assertTrue(isinstance(a, AdminSection))
        self.assertEqual(a.__str__(), a.name)


class AdminEntryTestCase(TestCase):
    def test_creation(self):
        a = AdminEntryFactory()
        self.assertTrue(isinstance(a, AdminEntry))
        self.assertEqual(a.__str__(), "%s %s" % (a.package, a.model))

    def test_admin_url(self):
        a = AdminEntryFactory(package='utils', model='adminentry')
        request_factory = RequestFactory()
        request = request_factory.get('/')
        self.assertEqual('http://testserver/admin/utils/adminentry/',
                         a.admin_url(request))
