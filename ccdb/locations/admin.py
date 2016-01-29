from django.contrib import admin

from .models import Region, Site, MunicipalLocation, \
    StudyLocation, StorageLocation


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code')
    list_per_page = 25
    fields = ('name', 'code', 'sort_order')


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'region_name', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'region__name', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'region', 'description', 'sort_order')

    def region_name(self, obj):
        return obj.region.name
    region_name.admin_order_field = 'region__name'
    region_name.short_description = 'Region'


class MunicipalLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'site_name', 'municipal_location_type',
        'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'site__name', 'municipal_location_type',
        'description')
    list_per_page = 25
    fields = ('name', 'code', 'site', 'municipal_location_type',
        'description', 'sort_order')

    def site_name(self, obj):
        return obj.site.name
    site_name.admin_order_field = 'site__name'
    site_name.short_description = 'Site'


class StudyLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'site_name', 'study_location_type',
        'treatment_type', 'ml_name', 'collecting_location',
        'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'site__name', 'study_location_type',
        'treatment_type', 'municipal_location__name', 'collecting_location',
        'description')
    list_per_page = 25
    fields = ('name', 'code', 'site', 'study_location_type',
        'treatment_type', 'municipal_location', 'collecting_location',
        'description', 'sort_order')

    def site_name(self, obj):
        return obj.site.name
    site_name.admin_order_field = 'site__name'
    site_name.short_description = 'Site'

    def ml_name(self, obj):
        if obj.municipal_location:
            return obj.municipal_location.name
        return obj.municipal_location
    ml_name.admin_order_field = 'municipal_location__name'
    ml_name.short_description = 'Municipal Location'


class StorageLocationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'facility', 'building', 'room', 'freezer', 'temp_c',
        'description', 'sort_order')
    list_display_links = ('__str__',)
    search_fields = ('__str__', 'facility', 'building', 'room', 'freezer', 'temp_c',
        'description')
    list_per_page = 25
    fields = ('facility', 'building', 'room', 'freezer', 'temp_c',
        'description', 'sort_order')



admin.site.register(Region, RegionAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(MunicipalLocation, MunicipalLocationAdmin)
admin.site.register(StudyLocation, StudyLocationAdmin)
admin.site.register(StorageLocation, StorageLocationAdmin)
