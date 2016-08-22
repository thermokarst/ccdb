from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from ..models import GrantReport
from ..admin import GrantReportAdmin
from .factories import GrantReportFactory


class GrantReportAdminTests(TestCase):
    def setUp(self):
        self.grant_report = GrantReportFactory()
        self.site = AdminSite()

    def test_list_display(self):
        admin_obj = GrantReportAdmin(GrantReport, self.site)
        self.assertEqual(admin_obj.check(), [])

        grant_title_from_callable = admin_obj.grant_title(self.grant_report)
        self.assertEqual(grant_title_from_callable,
                         self.grant_report.grant.title)
