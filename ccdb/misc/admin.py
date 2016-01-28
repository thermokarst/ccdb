from django.contrib import admin

from .models import MeasurementUnit, MeasurementType, Container, Material, Color


class MeasurementUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'unit_class', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'unit_class', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'unit_class', 'description', 'sort_order')


class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'measurement_type_class', 'description',
        'default_measurement_unit', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'measurement_type_class', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'measurement_type_class', 'description',
        'default_measurement_unit', 'sort_order')


class ContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'application', 'color', 'material',
        'volume', 'measurement_unit', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'application', 'color', 'material',
        'volume', 'measurement_unit')
    list_per_page = 25
    fields = ('name', 'code', 'application', 'color', 'material',
        'volume', 'measurement_unit', 'sort_order')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'material_class', 'description', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'material_class', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'material_class', 'description', 'sort_order')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'color_number', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'color_number')
    list_per_page = 25
    fields = ('name', 'code', 'color_number', 'sort_order')


admin.site.register(MeasurementUnit, MeasurementUnitAdmin)
admin.site.register(MeasurementType, MeasurementTypeAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Color, ColorAdmin)
