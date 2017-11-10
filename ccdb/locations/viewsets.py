from rest_framework import viewsets

from .models import Region, Site, StudyLocation
from .serializers import (
    RegionSerializer, SiteSerializer, StudyLocationSerializer)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class StudyLocationViewSet(viewsets.ModelViewSet):
    queryset = StudyLocation.objects.all()
    serializer_class = StudyLocationSerializer
