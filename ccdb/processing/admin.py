from django.contrib import admin

from .models import ProcessType, Reagent, Flaw


class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'description', 'sort_order')


class ReagentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'reagent_class', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'reagent_class')
    list_per_page = 25
    fields = ('name', 'code', 'reagent_class', 'sort_order')


class FlawAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 25
    fields = ('name', 'description')


admin.site.register(ProcessType, ProcessTypeAdmin)
admin.site.register(Reagent, ReagentAdmin)
admin.site.register(Flaw, FlawAdmin)
