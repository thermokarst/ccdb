from django.db import models

from autoslug import AutoSlugField


class CollectionType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class CollectionMethod(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    collection_method_class = models.CharField(max_length=50, blank=True)
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


class ADFGPermit(models.Model):
    name = models.CharField(max_length=200)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']


class Collection(models.Model):
    project = models.ForeignKey('projects.Project')
    study_location = models.ForeignKey('locations.StudyLocation')
    collection_type = models.ForeignKey(CollectionType)
    collection_method = models.ForeignKey(CollectionMethod)
    number_of_traps = models.IntegerField(blank=True, null=True)
    collection_start_date = models.DateField(blank=True, null=True)
    collection_start_time = models.TimeField(blank=True, null=True)
    collection_end_date = models.DateField(blank=True, null=True)
    collection_end_time = models.TimeField(blank=True, null=True)
    storage_location = models.ForeignKey('locations.StorageLocation', blank=True, null=True)
    specimen_state = models.CharField(max_length=50, blank=True)
    process_type = models.ForeignKey('processing.ProcessType', blank=True, null=True)
    reagent = models.ForeignKey('processing.Reagent', blank=True, null=True)
    adfg_permit = models.ForeignKey(ADFGPermit, blank=True, null=True)
    flaw = models.ForeignKey(Flaw, blank=True, null=True)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.project, self.study_location,
            self.collection_start_date, self.collection_end_date,
            self.collection_type, self.collection_method)

    class Meta:
        unique_together = ('project', 'study_location', 'collection_type',
            'collection_start_date', 'collection_end_date', 'collection_method')


class DatasheetAttachment(models.Model):
    collection = models.ForeignKey(Collection)
    datasheet = models.FileField("Datasheet",
        upload_to='collections/datasheets/%Y/%m/%d')


class CollectionTrap(models.Model):
    collection = models.ForeignKey(Collection)
    number_of_traps = models.IntegerField()
    date_opened = models.DateField()
    time_opened = models.TimeField()
    date_closed = models.DateField()
    time_closed = models.TimeField()

    def __str__(self):
        return "{collection} {number_of_traps} {date_opened} {date_closed}".format(self)

    class Meta:
        unique_together = ('collection', 'date_opened', 'time_opened', 'date_closed', 'time_closed')
