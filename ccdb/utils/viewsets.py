from rest_framework import viewsets

from .models import AdminSection, AdminEntry
from .serializers import AdminSectionSerializer, AdminEntrySerializer


class AdminSectionViewSet(viewsets.ModelViewSet):
    queryset = AdminSection.objects.all()
    serializer_class = AdminSectionSerializer


class AdminEntryViewSet(viewsets.ModelViewSet):
    queryset = AdminEntry.objects.all()
    serializer_class = AdminEntrySerializer

    def get_serializer_context(self):
        return {'request': self.request}
