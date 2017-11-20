from rest_framework_json_api import serializers

from .models import (ADFGPermit, Collection, CollectionMethod, CollectionType,
                     Flaw)


class CollectionSerializer(serializers.ModelSerializer):
    included_serializers = {
        'adfg_permit':
            'ccdb.collections_ccdb.serializers.ADFGPermitSerializer',
        'project': 'ccdb.projects.serializers.ProjectSerializer',
        'site': 'ccdb.locations.serializers.SiteSerializer',
        'study_location': 'ccdb.locations.serializers.StudyLocationSerializer',
        'collection_method':
            'ccdb.collections_ccdb.serializers.CollectionMethodSerializer',
        'collection_type':
            'ccdb.collections_ccdb.serializers.CollectionTypeSerializer',
        'flaw': 'ccdb.collections_ccdb.serializers.FlawSerializer',
        'collection_species':
            'ccdb.species.serializers.CollectionSpeciesSerializer',
    }

    class Meta:
        model = Collection
        fields = ('id', 'project', 'study_location', 'collection_type',
                  'collection_method', 'number_of_traps',
                  'collection_start_date', 'collection_start_time',
                  'collection_end_date', 'collection_end_time',
                  'storage_location', 'specimen_state', 'process_type',
                  'reagent', 'adfg_permit', 'flaw', 'display_name',
                  'collection_species')


class ADFGPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ADFGPermit
        fields = ('id', 'name', 'sort_order')


class CollectionMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionMethod
        fields = ('id', 'name', 'code', 'collection_method_class',
                  'sort_order')


class CollectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionType
        fields = ('id', 'name', 'code', 'sort_order')


class FlawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flaw
        fields = ('id', 'name', 'description', 'sort_order')
