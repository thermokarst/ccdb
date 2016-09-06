from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .factories import AdminSectionFactory, AdminEntryFactory
from ccdb.users.models import User


class AdminTestCase(APITestCase):
    def setUp(self):
        self.username = 'abc'
        self.password = '123'
        self.user = User.objects.create(username=self.username,
                                        password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.login(username=self.username, password=self.password)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token.key)


class AdminSectionTestCase(AdminTestCase):
    def test_list(self):
        AdminSectionFactory.create_batch(5)
        url = reverse('api:v1:adminsection-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)


class AdminEntryTestCase(AdminTestCase):
    def test_list(self):
        AdminEntryFactory.create_batch(5, package='utils', model='adminentry')
        url = reverse('api:v1:adminentry-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)
