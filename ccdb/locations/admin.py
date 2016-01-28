from django.contrib import admin

from .models import Region, Site, MunicipalLocation, \
    StudyLocation, StorageLocation


admin.site.register(Region)
admin.site.register(Site)
admin.site.register(MunicipalLocation)
admin.site.register(StudyLocation)
admin.site.register(StorageLocation)
