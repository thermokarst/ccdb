from django.db import models

from autoslug import AutoSlugField


class ProcessType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class Reagent(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    reagent_class = models.CharField(max_length=50, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class Flaw(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']


class Processing(models.Model):
    process_type = models.ForeignKey(ProcessType, related_name='processings')
    container = models.ForeignKey('misc.Container', related_name='processings')
    container_label = models.CharField(max_length=50)
    process_date = models.DateField(blank=True, null=True)
    process_time = models.TimeField(blank=True, null=True)
    reagent = models.ForeignKey(Reagent, blank=True, null=True,
                                related_name='processings')
    reagent_volume = models.FloatField(blank=True, null=True)
    measurement_unit = models.ForeignKey('misc.MeasurementUnit', blank=True,
                                         null=True, related_name='processings')
    minutes_in_reagent = models.IntegerField(blank=True, null=True)
    flaw = models.ForeignKey(Flaw, blank=True, null=True, related_name='processings')

    def __str__(self):
        return "{} {} {}".format(self.process_date, self.process_type, self.container_label)

    class Meta:
        unique_together = ('process_type', 'container', 'container_label',
                           'process_date', 'process_time', 'reagent')
