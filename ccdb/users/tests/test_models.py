from django.test import TestCase
from django.db import IntegrityError, transaction

from ..models import User
from ..factories import UserFactory


class UserTestCase(TestCase):
    def test_creation(self):
        u = UserFactory()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__str__(), u.username)

    def test_uniqueness(self):
        u1 = UserFactory()
        with transaction.atomic(), self.assertRaises(IntegrityError):
            UserFactory(username=u1.username)
        u3 = UserFactory()
        self.assertTrue(isinstance(u3, User))
