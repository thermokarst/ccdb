from django.db import models

from autoslug import AutoSlugField


# class Collection(models.Model):
#     project = models.ForeignKey('projects.Project')
#     study_location = models.ForeignKey('locations.StudyLocation')
#     collection_type = models.ForeignKey(CollectionType)
#     collection_method = models.ForeignKey(CollectionMethod)
#     number_of_traps = models.IntegerField(blank=True, null=True)
#     collection_start_date = models.DateField(blank=True, null=True)
#     collection_start_time = models.TimeField(blank=True, null=True)
#     collection_end_date = models.DateField(blank=True, null=True)
#     collection_end_time = models.TimeField(blank=True, null=True)
#     storage_location = models.ForeignKey('locations.StorageLocation', blank=True, null=True)
#     specimen_state = models.CharField(max_length=50, blank=True)
#     process_type = models.ForeignKey('processing.ProcessType', blank=True, null=True)
#     reagent = models.ForeignKey('processing.Reagent', blank=True, null=True)
#     # adfg_permit = models.CharField(db_column='ADFG_Permit', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     # link_to_datasheets = models.CharField(db_column='Link_To_Datasheets', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     flaw = models.ForeignKey(Flaw, blank=True, null=True)
#
#     def __str__(self):
#         return "{project} {study_location} {collection_type} {collection_method}".format(**self)
#
#     class Meta:
#         unique_together = ('project', 'study_location', 'collection_type',
#             'collection_start_date', 'collection_end_date', 'collection_method')
