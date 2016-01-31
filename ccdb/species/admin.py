from django.contrib import admin

from .models import Species


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'genus', 'species', 'parasite', 'sort_order')
    list_display_links = ('common_name',)
    search_fields = ('common_name', 'genus', 'species', 'parasite')
    list_per_page = 25
    fields = ('common_name', 'genus', 'species', 'parasite', 'sort_order')


admin.site.register(Species, SpeciesAdmin)
