from django.contrib import admin

from .models import Project, Grant, GrantReport


class ProjectGrantInline(admin.TabularInline):
    model = Grant.projects.through
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'iacuc_number', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'iacuc_number', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'iacuc_number', 'description', 'sort_order')

    inlines = [ProjectGrantInline]


class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'description', 'sort_order')
    list_display_links = ('title',)
    search_fields = ('title', 'code', 'description', 'description')
    list_per_page = 25
    fields = ('title', 'code', 'description', 'projects', 'sort_order')


class GrantReportAdmin(admin.ModelAdmin):
    list_display = ('grant', 'title', 'report_type', 'description', 'due_date',
        'submitted_date', 'attachment', 'sort_order')
    list_display_links = ('title',)
    search_fields = ('grant__title', 'title', 'report_type', 'description', 'due_date',
        'submitted_date', 'attachment')
    list_per_page = 25
    fields = ('title', 'report_type', 'description', 'due_date',
        'submitted_date', 'attachment', 'sort_order')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(GrantReport, GrantReportAdmin)
