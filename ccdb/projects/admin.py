from django.contrib import admin

from .models import Project, Grant, GrantReport


class ProjectGrantInline(admin.TabularInline):
    model = Grant.projects.through
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'iacuc_number', 'description', 'sort_order')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'code', 'iacuc_number', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'iacuc_number', 'description', 'sort_order')

    inlines = [ProjectGrantInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Grant)
admin.site.register(GrantReport)
