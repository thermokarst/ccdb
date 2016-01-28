from django.contrib import admin

from .models import MeasurementUnit, MeasurementType, Container, Material, Color

admin.site.register(MeasurementUnit)
admin.site.register(MeasurementType)
admin.site.register(Container)
admin.site.register(Material)
admin.site.register(Color)
