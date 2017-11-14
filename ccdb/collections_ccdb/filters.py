from django_filters.filters import ModelMultipleChoiceFilter
from django_filters import rest_framework as filters

from .models import Collection, CollectionMethod, ADFGPermit
from ccdb.projects.models import Project
from ccdb.locations.models import Region, Site, StudyLocation


class CollectionFilter(filters.FilterSet):
    project = ModelMultipleChoiceFilter(
        name='project__id',
        to_field_name='id',
        queryset=Project.objects.all(),
    )

    region = ModelMultipleChoiceFilter(
        name='study_location__site__region__id',
        to_field_name='id',
        queryset=Region.objects.all(),
    )

    site = ModelMultipleChoiceFilter(
        name='study_location__site__id',
        to_field_name='id',
        queryset=Site.objects.all(),
    )

    study_location = ModelMultipleChoiceFilter(
        name='study_location__id',
        to_field_name='id',
        queryset=StudyLocation.objects.all(),
    )

    collection_method = ModelMultipleChoiceFilter(
        name='collection_method__id',
        to_field_name='id',
        queryset=CollectionMethod.objects.all(),
    )

    adfg_permit = ModelMultipleChoiceFilter(
        name='adfg_permit__id',
        to_field_name='id',
        queryset=ADFGPermit.objects.all(),
    )

    class Meta:
        model = Collection
        fields = ['project', 'region', 'site', 'study_location',
                  'collection_method', 'number_of_traps',
                  'collection_start_date', 'collection_end_date',
                  'adfg_permit']
