from rest_framework_json_api import serializers

from .models import Species, Sex, CollectionSpecies


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('common_name', 'genus', 'species', 'parasite', 'sort_order')


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = ('name', 'sort_order')


class CollectionSpeciesSerializer(serializers.ModelSerializer):
    included_serializers = {
        'collection': 'ccdb.collections_ccdb.serializers.CollectionSerializer',
        'species': 'ccdb.species.serializers.SpeciesSerializer',
        'sex': 'ccdb.species.serializers.SexSerializer',
    }

    class Meta:
        model = CollectionSpecies
        fields = ('id', 'sex', 'count', 'count_estimated', 'collection',
                  'species')
