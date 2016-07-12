from django.contrib import admin

from .models import (CollectionType, CollectionMethod, Flaw, ADFGPermit,
                     DatasheetAttachment, CollectionTrap, Collection)
from ..species.models import CollectionSpecies


class CollectionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code')
    list_per_page = 25
    fields = ('name', 'code', 'sort_order')


class CollectionMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'collection_method_class', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'collection_method_class')
    list_per_page = 25
    fields = ('name', 'code', 'collection_method_class', 'sort_order')


class FlawAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 25
    fields = ('name', 'description')


class ADFGPermitAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25
    fields = ('name', 'sort_order')


class DatasheetAttachmentAdmin(admin.ModelAdmin):
    list_display = ('collection', 'datasheet')
    list_display_links = ('datasheet',)
    list_per_page = 25
    fields = ('collection', 'datasheet')


class CollectionTrapAdmin(admin.ModelAdmin):
    list_display = ('collection', 'number_of_traps', 'date_opened',
                    'time_opened', 'date_closed', 'time_closed')
    list_display_links = ('number_of_traps',)
    list_per_page = 25
    fields = ('collection', 'number_of_traps', 'date_opened',
              'time_opened', 'date_closed', 'time_closed')


class CollectionSpeciesInlineAdmin(admin.TabularInline):
    model = CollectionSpecies


class CollectionAdmin(admin.ModelAdmin):
    inlines = (CollectionSpeciesInlineAdmin, )
    list_display = ('project', 'study_location', 'collection_end_date',
                    'collection_type', 'collection_method')
    list_display_links = ('project', 'study_location', 'collection_end_date',
                          'collection_type', 'collection_method')
    list_filter = ('project', 'study_location', 'collection_type',
                   'collection_method')


admin.site.register(CollectionType, CollectionTypeAdmin)
admin.site.register(CollectionMethod, CollectionMethodAdmin)
admin.site.register(Flaw, FlawAdmin)
admin.site.register(ADFGPermit, ADFGPermitAdmin)
admin.site.register(DatasheetAttachment, DatasheetAttachmentAdmin)
admin.site.register(CollectionTrap, CollectionTrapAdmin)
admin.site.register(Collection, CollectionAdmin)
