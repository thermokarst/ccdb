from rest_framework import viewsets

from .models import Species, CollectionSpecies
from .serializers import SpeciesSerializer, CollectionSpeciesSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class CollectionSpeciesViewSet(viewsets.ModelViewSet):
    queryset = CollectionSpecies.objects.all()
    serializer_class = CollectionSpeciesSerializer
