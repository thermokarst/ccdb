from rest_framework import viewsets
from django_filters import rest_framework as filters

from .filters import CollectionFilter
from .models import (ADFGPermit, Collection, CollectionMethod, CollectionType,
                     Flaw, DatasheetAttachment, CollectionMeasurement)
from .serializers import (CollectionSerializer, CollectionMethodSerializer,
                          CollectionTypeSerializer, FlawSerializer,
                          ADFGPermitSerializer, DatasheetAttachmentSerializer,
                          CollectionMeasurementSerializer)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CollectionFilter


class CollectionMethodViewSet(viewsets.ModelViewSet):
    queryset = CollectionMethod.objects.all()
    serializer_class = CollectionMethodSerializer


class CollectionTypeViewSet(viewsets.ModelViewSet):
    queryset = CollectionType.objects.all()
    serializer_class = CollectionTypeSerializer


class FlawViewSet(viewsets.ModelViewSet):
    queryset = Flaw.objects.all()
    serializer_class = FlawSerializer


class ADFGPermitViewSet(viewsets.ModelViewSet):
    queryset = ADFGPermit.objects.all()
    serializer_class = ADFGPermitSerializer


class DatasheetAttachmentViewSet(viewsets.ModelViewSet):
    queryset = DatasheetAttachment.objects.all()
    serializer_class = DatasheetAttachmentSerializer


class CollectionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = CollectionMeasurement.objects.all()
    serializer_class = CollectionMeasurementSerializer
