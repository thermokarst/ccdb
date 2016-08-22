from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from ..models import MeasurementType, Container
from ..admin import MeasurementTypeAdmin, ContainerAdmin
from .factories import MeasurementTypeFactory, ContainerFactory


class MeasurementTypeAdminTests(TestCase):
    def setUp(self):
        self.mu = MeasurementTypeFactory()
        self.site = AdminSite()

    def test_list_display(self):
        admin_obj = MeasurementTypeAdmin(MeasurementType, self.site)
        self.assertEqual(admin_obj.check(), [])

        mu_code_from_callable = admin_obj.measurement_unit_code(self.mu)
        self.assertEqual(mu_code_from_callable,
                         self.mu.default_measurement_unit.code)


class ContainerAdminTests(TestCase):
    def setUp(self):
        self.container = ContainerFactory()
        self.site = AdminSite()

    def test_list_display(self):
        admin_obj = ContainerAdmin(Container, self.site)
        self.assertEqual(admin_obj.check(), [])

        color_name_from_callable = admin_obj.color_name(self.container)
        self.assertEqual(color_name_from_callable, self.container.color.name)

        material_name_from_callable = admin_obj.material_name(self.container)
        self.assertEqual(material_name_from_callable,
                         self.container.material.name)

        mu_name_from_callable = admin_obj.measurement_unit_name(self.container)
        self.assertEqual(mu_name_from_callable,
                         self.container.measurement_unit.name)
