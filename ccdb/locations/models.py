from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class Site(models.Model):
    region = models.ForeignKey(Region, blank=True, null=True,
                               related_name='sites', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('region', 'name', 'code')
        ordering = ['sort_order']


class MunicipalLocation(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    municipal_location_type = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class StudyLocation(models.Model):
    site = models.ForeignKey(Site, related_name='study_locations',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    study_location_type = models.CharField(max_length=50, blank=True)
    treatment_type = models.CharField(max_length=100, blank=True)
    municipal_location = models.ForeignKey(MunicipalLocation,
                                           blank=True, null=True,
                                           related_name='study_locations',
                                           on_delete=models.CASCADE)
    collecting_location = models.BooleanField(default=False)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.code

    class Meta:
        unique_together = ('site', 'name')
        ordering = ['sort_order']


class StorageLocation(models.Model):
    code = models.CharField(max_length=100)
    facility = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    room = models.CharField(max_length=50, blank=True)
    freezer = models.CharField(max_length=50, blank=True)
    temp_c = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.code

    class Meta:
        unique_together = ('code', 'facility', 'building', 'room',
                           'freezer', 'temp_c')
        ordering = ['sort_order']
