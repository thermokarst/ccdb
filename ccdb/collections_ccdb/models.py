from django.db import models

from autoslug import AutoSlugField


class Collection(models.Model):
    projectid = models.ForeignKey('TblLuProjects', db_column='ProjectID')  # Field name made lowercase.
    collectionid = models.AutoField(db_column='CollectionID', primary_key=True)  # Field name made lowercase.
    study_locationid = models.ForeignKey('TblLuStudyLocations', db_column='Study_LocationID')  # Field name made lowercase.
    collection_typeid = models.ForeignKey('TblLuCollectionTypes', db_column='Collection_TypeID')  # Field name made lowercase.
    collection_methodid = models.ForeignKey('TblLuCollectionMethods', db_column='Collection_MethodID')  # Field name made lowercase.
    number_of_traps = models.IntegerField(db_column='Number_Of_Traps', blank=True, null=True)  # Field name made lowercase.
    collection_start_date = models.DateField(db_column='Collection_Start_Date', blank=True, null=True)  # Field name made lowercase.
    collection_start_time = models.TimeField(db_column='Collection_Start_Time', blank=True, null=True)  # Field name made lowercase.
    collection_end_date = models.DateField(db_column='Collection_End_Date', blank=True, null=True)  # Field name made lowercase.
    collection_end_time = models.TimeField(db_column='Collection_End_Time', blank=True, null=True)  # Field name made lowercase.
    storage_locationid = models.ForeignKey('TblLuStorageLocations', db_column='Storage_LocationID', blank=True, null=True)  # Field name made lowercase.
    specimen_state = models.CharField(db_column='Specimen_State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    process_typeid = models.ForeignKey('TblLuProcessTypes', db_column='Process_TypeID', blank=True, null=True)  # Field name made lowercase.
    reagentid = models.ForeignKey('TblLuReagents', db_column='ReagentID', blank=True, null=True)  # Field name made lowercase.
    adfg_permit = models.CharField(db_column='ADFG_Permit', max_length=25, blank=True, null=True)  # Field name made lowercase.
    link_to_datasheets = models.CharField(db_column='Link_To_Datasheets', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Collections'
        unique_together = (('ProjectID', 'Study_LocationID', 'Collection_TypeID', 'Collection_Start_Date', 'Collection_End_Date', 'Collection_MethodID'),)
