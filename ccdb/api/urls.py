from django.conf.urls import url, include

from rest_framework import routers

from . import views as api_v
from ..utils import viewsets as utils_viewsets
from ..collections_ccdb import viewsets as collections_viewsets
from ..projects import viewsets as projects_viewsets
from ..locations import viewsets as locations_viewsets
from ..species import viewsets as species_viewsets


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'admin-sections', utils_viewsets.AdminSectionViewSet)
router.register(r'admin-entries', utils_viewsets.AdminEntryViewSet)
# Collections
router.register(r'collections', collections_viewsets.CollectionViewSet)
router.register(r'collection-methods',
                collections_viewsets.CollectionMethodViewSet)
router.register(r'collection-types',
                collections_viewsets.CollectionTypeViewSet)
router.register(r'collection-flaws',
                collections_viewsets.FlawViewSet)
router.register(r'collection-measurements',
                collections_viewsets.CollectionMeasurementViewSet)
router.register(r'adfg-permits', collections_viewsets.ADFGPermitViewSet)
router.register(r'datasheet-attachments',
                collections_viewsets.DatasheetAttachmentViewSet)
# Projects
router.register(r'projects', projects_viewsets.ProjectViewSet)
# Locations
router.register(r'regions', locations_viewsets.RegionViewSet)
router.register(r'sites', locations_viewsets.SiteViewSet)
router.register(r'study-locations', locations_viewsets.StudyLocationViewSet)
# Species
router.register(r'species', species_viewsets.SpeciesViewSet)
router.register(r'sexes', species_viewsets.SexViewSet)
router.register(r'collection-species',
                species_viewsets.CollectionSpeciesViewSet)

app_name = 'api'
urlpatterns = [
    url(r'^auth/login/', api_v.Login.as_view()),
    url(r'^auth/password/reset/confirm/',
        api_v.PasswordResetConfirm.as_view()),
    url(r'^auth/password/reset/', api_v.PasswordReset.as_view()),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^v1/', include((router.urls, 'api_v1'), namespace='v1')),
]
