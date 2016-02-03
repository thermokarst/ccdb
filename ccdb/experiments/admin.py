from django.contrib import admin

from .models import Flaw, Experiment, ProtocolAttachment, TreatmentType, \
    Treatment, TreatmentReplicate, AliveDeadCount


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
    fields = ('name', 'code', 'description', 'flaw', 'collections', 'sort_order')


class ProtocolAttachmentAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'protocol')
    list_display_links = ('protocol',)
    search_fields = ('protocol',)
    list_per_page = 25
    fields = ('experiment', 'protocol')


class TreatmentTypeAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'name', 'code', 'treatment_type',
        'placement', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('experiment', 'name', 'code', 'treatment_type',
        'placement', 'description')
    list_per_page = 25
    fields = ('experiment', 'name', 'code', 'treatment_type', 'placement',
        'description', 'sort_order')


class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment_type', 'container', 'study_location', 'species',
        'sex', 'flaw')
    list_display_links = ('treatment_type',)
    search_fields = ('treatment_type', 'container', 'study_location', 'species',
        'sex', 'flaw')
    list_per_page = 25
    fields = ('treatment_type', 'container', 'study_location', 'species',
        'sex', 'flaw')


class TreatmentReplicateAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'name', 'setup_date', 'setup_time',
        'setup_sample_size', 'mass_g', 'flaw')
    list_display_links = ('name',)
    search_fields = ('treatment', 'name', 'setup_date', 'setup_time',
        'setup_sample_size', 'mass_g', 'flaw')
    list_per_page = 25
    fields = ('treatment', 'name', 'setup_date', 'setup_time',
        'setup_sample_size', 'mass_g', 'flaw')


class AliveDeadCountAdmin(admin.ModelAdmin):
    list_display = ('treatment', 'tr', 'status_date',
        'status_time', 'count_alive', 'count_dead', 'flaw')
    list_display_links = ('status_date',)
    search_fields = ('treatment_replicate', 'status_date', 'status_time',
        'count_alive', 'count_dead', 'flaw')
    list_per_page = 25
    fields = ('treatment_replicate', 'status_date', 'status_time',
        'count_alive', 'count_dead', 'flaw')

    def treatment(self, obj):
        return obj.treatment_replicate.treatment
    treatment.admin_order_field = 'treatment_replicate__treatment'

    def tr(self, obj):
        return "{}_{}_{}".format(obj.treatment_replicate.setup_date,
            obj.treatment_replicate.name,
            obj.treatment_replicate.setup_sample_size)
    tr.short_description = 'Treatment Replicate'


admin.site.register(Flaw, FlawAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(ProtocolAttachment, ProtocolAttachmentAdmin)
admin.site.register(TreatmentType, TreatmentTypeAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(TreatmentReplicate, TreatmentReplicateAdmin)
admin.site.register(AliveDeadCount, AliveDeadCountAdmin)
