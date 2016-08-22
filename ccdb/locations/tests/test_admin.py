from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from ..models import Site, StudyLocation
from ..admin import SiteAdmin, StudyLocationAdmin
from .factories import SiteFactory, StudyLocationFactory


class SiteAdminTests(TestCase):
    def setUp(self):
        self.site = SiteFactory()
        self.admin_site = AdminSite()

    def test_list_display(self):
        admin_obj = SiteAdmin(Site, self.admin_site)
        self.assertEqual(admin_obj.check(), [])

        region_name_from_callable = admin_obj.region_name(self.site)
        self.assertEqual(region_name_from_callable,
                         self.site.region.name)


class StudyLocationAdminTests(TestCase):
    def setUp(self):
        self.sl = StudyLocationFactory()
        self.site = AdminSite()

    def test_list_display(self):
        admin_obj = StudyLocationAdmin(StudyLocation, self.site)
        self.assertEqual(admin_obj.check(), [])

        site_name_from_callable = admin_obj.site_name(self.sl)
        self.assertEqual(site_name_from_callable,
                         self.sl.site.name)

        ml_name_from_callable = admin_obj.ml_name(self.sl)
        self.assertEqual(ml_name_from_callable,
                         str(self.sl.municipal_location))
