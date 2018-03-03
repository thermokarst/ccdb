from django.contrib import admin

from .models import Species, Sex, TrapSpecies, CollectionSpecies


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'genus', 'species', 'parasite',
                    'sort_order')
    list_display_links = ('common_name',)
    search_fields = ('common_name', 'genus', 'species', 'parasite')
    list_per_page = 25
    fields = ('common_name', 'genus', 'species', 'parasite', 'sort_order')


class SexAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25
    fields = ('name', 'sort_order')


class TrapSpeciesAdmin(admin.ModelAdmin):
    list_display = ('collection_trap', 'species', 'sex', 'count',
                    'count_estimated')
    list_display_links = ('count',)
    search_fields = ('collection_trap', 'species', 'sex', 'count',
                     'count_estimated')
    list_per_page = 25
    fields = ('collection_trap', 'species', 'sex', 'count', 'count_estimated')


class CollectionSpeciesAdmin(admin.ModelAdmin):
    list_display = ('collection', 'species', 'sex', 'count', 'count_estimated')
    list_display_links = ('count',)
    search_fields = ('collection', 'species', 'sex', 'count',
                     'count_estimated')
    list_per_page = 25
    fields = ('collection', 'species', 'sex', 'count', 'count_estimated')


admin.site.register(Species, SpeciesAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(TrapSpecies, TrapSpeciesAdmin)
admin.site.register(CollectionSpecies, CollectionSpeciesAdmin)
