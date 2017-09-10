from rest_framework import viewsets

from .models import Collection, CollectionMethod, CollectionType, Flaw
from .serializers import (CollectionSerializer, CollectionMethodSerializer,
                          CollectionTypeSerializer, FlawSerializer)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CollectionMethodViewSet(viewsets.ModelViewSet):
    queryset = CollectionMethod.objects.all()
    serializer_class = CollectionMethodSerializer


class CollectionTypeViewSet(viewsets.ModelViewSet):
    queryset = CollectionType.objects.all()
    serializer_class = CollectionTypeSerializer


class FlawViewSet(viewsets.ModelViewSet):
    queryset = Flaw.objects.all()
    serializer_class = FlawSerializer
