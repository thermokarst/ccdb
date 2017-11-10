from rest_framework import serializers

from .models import Region, Site, StudyLocation


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'code', 'sort_order')


class SiteSerializer(serializers.ModelSerializer):
    included_serializers = {
        'region': 'ccdb.locations.serializers.RegionSerializer',
    }

    class Meta:
        model = Site
        fields = ('name', 'code', 'description', 'sort_order', 'region')


class StudyLocationSerializer(serializers.ModelSerializer):
    included_serializers = {
        'site': 'ccdb.locations.serializers.SiteSerializer',
    }

    class Meta:
        model = StudyLocation
        fields = ('name', 'code', 'study_location_type', 'treatment_type',
                  'collecting_location', 'description', 'sort_order', 'site')
