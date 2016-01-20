from django.contrib import admin

from .models import Project, Grant


admin.site.register(Project)
admin.site.register(Grant)
