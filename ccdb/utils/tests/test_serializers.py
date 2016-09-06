from django.test import TestCase
from django.test.client import RequestFactory

from .factories import AdminSectionFactory, AdminEntryFactory
from ..serializers import AdminSectionSerializer, AdminEntrySerializer


class AdminSectionTestCase(TestCase):
    def test_creation(self):
        a = AdminSectionFactory()
        serializer = AdminSectionSerializer(a)
        data = {'name': a.name, 'id': a.id, 'sort': a.sort}
        self.assertEqual(data, serializer.data)


class AdminEntryTestCase(TestCase):
    def test_creation(self):
        a = AdminEntryFactory(package='utils', model='adminentry')
        request_factory = RequestFactory()
        request = request_factory.get('/')
        serializer = AdminEntrySerializer(a, context={'request': request})
        data = {'package': a.package, 'id': a.id, 'sort': a.sort,
                'model': a.model, 'section': a.section.id,
                'admin_url': a.admin_url(request)}
        self.assertEqual(data, serializer.data)
