from django.db import models


class CollectionType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

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

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class Flaw(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']


class ADFGPermit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']
        verbose_name = 'ADFG Permit'

    class JSONAPIMeta:
        resource_name = 'AdfgPermit'


class Collection(models.Model):
    project = models.ForeignKey('projects.Project', related_name='collections')
    study_location = models.ForeignKey('locations.StudyLocation',
                                       related_name='collections')
    collection_type = models.ForeignKey(CollectionType,
                                        related_name='collections')
    collection_method = models.ForeignKey(CollectionMethod,
                                          related_name='collections')
    number_of_traps = models.IntegerField(blank=True, null=True)
    collection_start_date = models.DateField(blank=True, null=True)
    collection_start_time = models.TimeField(blank=True, null=True)
    collection_end_date = models.DateField(blank=True, null=True)
    collection_end_time = models.TimeField(blank=True, null=True)
    storage_location = models.ForeignKey('locations.StorageLocation',
                                         blank=True, null=True,
                                         related_name='collections')
    specimen_state = models.CharField(max_length=50, blank=True)
    process_type = models.ForeignKey('processing.ProcessType', blank=True,
                                     null=True, related_name='collections')
    reagent = models.ForeignKey('processing.Reagent', blank=True, null=True,
                                related_name='collections')
    adfg_permit = models.ForeignKey(ADFGPermit, blank=True, null=True,
                                    related_name='collections')
    flaw = models.ForeignKey(Flaw, blank=True, null=True,
                             related_name='collections')
    display_name = models.CharField(max_length=255, editable=False)

    def save(self, *args, **kwargs):
        self.display_name = "{}_{}_{}_{}".format(self.project,
                                                 self.collection_end_date,
                                                 self.study_location,
                                                 self.collection_type)
        super(Collection, self).save(*args, **kwargs)

    def __str__(self):
        return self.display_name

    class Meta:
        unique_together = ('project', 'study_location', 'collection_type',
                           'collection_start_date', 'collection_end_date',
                           'collection_method')
        ordering = ['project', 'collection_end_date']


class DatasheetAttachment(models.Model):
    collection = models.ForeignKey(Collection, related_name='datasheets')
    datasheet = models.FileField("Datasheet",
                                 upload_to='collections/datasheets/%Y/%m/%d')


class CollectionTrap(models.Model):
    collection = models.ForeignKey(Collection, related_name='traps')
    number_of_traps = models.IntegerField()
    date_opened = models.DateField()
    time_opened = models.TimeField()
    date_closed = models.DateField()
    time_closed = models.TimeField()

    def __str__(self):
        return "{} # Traps: {} {} {}".format(self.collection,
                                             self.number_of_traps,
                                             self.date_opened,
                                             self.date_closed)

    class Meta:
        unique_together = ('collection', 'date_opened', 'time_opened',
                           'date_closed', 'time_closed')
