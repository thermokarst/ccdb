from rest_framework import viewsets

from .models import StudyLocation
from .serializers import StudyLocationSerializer


class StudyLocationViewSet(viewsets.ModelViewSet):
    queryset = StudyLocation.objects.all()
    serializer_class = StudyLocationSerializer
