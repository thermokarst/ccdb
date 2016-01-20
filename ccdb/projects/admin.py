from django.contrib import admin

from .models import Project, Grant, GrantReport


admin.site.register(Project)
admin.site.register(Grant)
admin.site.register(GrantReport)
