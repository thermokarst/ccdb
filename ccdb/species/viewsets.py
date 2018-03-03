from rest_framework import viewsets

from .models import Species, Sex, CollectionSpecies
from .serializers import (SpeciesSerializer, SexSerializer,
                          CollectionSpeciesSerializer)


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class SexViewSet(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer


class CollectionSpeciesViewSet(viewsets.ModelViewSet):
    queryset = CollectionSpecies.objects.all()
    serializer_class = CollectionSpeciesSerializer
