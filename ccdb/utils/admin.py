from django.contrib import admin

from .models import AdminSection, AdminEntry


admin.site.register(AdminSection)
admin.site.register(AdminEntry)
