from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from ..models import AliveDeadCount
from ..admin import AliveDeadCountAdmin
from .factories import AliveDeadCountFactory


class AliveDeadCountAdminTests(TestCase):
    def setUp(self):
        self.ad_count = AliveDeadCountFactory()
        self.site = AdminSite()

    def test_list_display(self):
        admin_obj = AliveDeadCountAdmin(AliveDeadCount, self.site)
        self.assertEqual(admin_obj.check(), [])

        treatment_from_callable = admin_obj.treatment(self.ad_count)
        self.assertEqual(treatment_from_callable,
                         self.ad_count.treatment_replicate.treatment)

        tr_from_callable = admin_obj.tr(self.ad_count)
        _tr = self.ad_count.treatment_replicate
        tr_from_related = '_'.join([str(_tr.setup_date), _tr.name,
                                    str(_tr.setup_sample_size)])
        self.assertEqual(tr_from_callable, tr_from_related)
