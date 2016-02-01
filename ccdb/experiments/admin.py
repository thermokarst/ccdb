from django.contrib import admin

from .models import Flaw, Experiment, ProtocolAttachment


class FlawAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 25
    fields = ('name', 'description')


class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'description', 'flaw', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'description', 'flaw', 'sort_order')
    list_per_page = 25
    fields = ('name', 'code', 'description', 'flaw', 'sort_order')


class ProtocolAttachmentAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'protocol')
    list_display_links = ('protocol',)
    search_fields = ('protocol',)
    list_per_page = 25
    fields = ('experiment', 'protocol')


admin.site.register(Flaw, FlawAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(ProtocolAttachment, ProtocolAttachmentAdmin)
