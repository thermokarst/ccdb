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
        'measurement_unit_code', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'measurement_type_class',
        'default_measurement_unit__code', 'description')
    list_per_page = 25
    fields = ('name', 'code', 'measurement_type_class', 'description',
        'default_measurement_unit', 'sort_order')

    def measurement_unit_code(self, obj):
        if obj.default_measurement_unit:
            return obj.default_measurement_unit.code
        return obj.default_measurement_unit
    measurement_unit_code.admin_order_field = 'default_measurement_unit__code'
    measurement_unit_code.short_description = 'Default Measurement Unit'


class ContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'application', 'color_name', 'material_name',
        'volume', 'measurement_unit_name', 'sort_order')
    list_display_links = ('name',)
    search_fields = ('name', 'code', 'application', 'color__name',
        'material__name', 'volume', 'measurement_unit__name')
    list_per_page = 25
    fields = ('name', 'code', 'application', 'color', 'material',
        'volume', 'measurement_unit', 'sort_order')

    def color_name(self, obj):
        if obj.color:
            return obj.color.name
        return obj.color
    color_name.admin_order_field = 'color__name'
    color_name.short_description = 'Color'

    def material_name(self, obj):
        if obj.material:
            return obj.material.name
        return obj.material
    material_name.admin_order_field = 'material__name'
    material_name.short_description = 'Material'

    def measurement_unit_name(self, obj):
        if obj.measurement_unit:
            return obj.measurement_unit.name
        return obj.measurement_unit
    measurement_unit_name.admin_order_field = 'measurement_unit__name'
    measurement_unit_name.short_description = 'Measurement Unit'


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
