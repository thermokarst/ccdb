from rest_framework import serializers

from .models import StudyLocation


class StudyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLocation
        fields = ('name', 'code', 'study_location_type', 'treatment_type',
                  'collecting_location', 'description', 'sort_order')
