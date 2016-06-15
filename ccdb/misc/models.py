from django.db import models


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)
    unit_class = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.code

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class MeasurementType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    measurement_type_class = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    default_measurement_unit = models.ForeignKey('MeasurementUnit', blank=True,
                                                 null=True,
                                                 related_name='measurement_types')
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']


class Material(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    material_class = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class Color(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, blank=True)
    color_number = models.FloatField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code', 'color_number')
        ordering = ['sort_order']


class Container(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    application = models.CharField(max_length=50, blank=True)
    color = models.ForeignKey(Color, blank=True, null=True,
                              related_name='containers')
    material = models.ForeignKey(Material, blank=True, null=True,
                                 related_name='containers')
    volume = models.FloatField(blank=True, null=True)
    measurement_unit = models.ForeignKey(MeasurementUnit, blank=True, null=True,
                                         related_name='containers')
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']
