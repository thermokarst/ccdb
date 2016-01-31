# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class TblAliveDeadCounts(models.Model):
    trrepid = models.ForeignKey('TblTreatmentReplicates', db_column='TrRepID')  # Field name made lowercase.
    alivedeadcountid = models.AutoField(db_column='AliveDeadCountID', primary_key=True)  # Field name made lowercase.
    status_date = models.DateField(db_column='Status_Date')  # Field name made lowercase.
    status_time = models.TimeField(db_column='Status_Time', blank=True, null=True)  # Field name made lowercase.
    count_alive = models.IntegerField(db_column='Count_Alive', blank=True, null=True)  # Field name made lowercase.
    count_dead = models.IntegerField(db_column='Count_Dead', blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Alive_Dead_Counts'


class TblBiorepImageHistology(models.Model):
    imageid = models.AutoField(db_column='ImageID', primary_key=True)  # Field name made lowercase.
    record_typeid = models.ForeignKey('TblLuRecordTypes', db_column='Record_TypeID')  # Field name made lowercase.
    foreign_key = models.IntegerField(db_column='Foreign_Key')  # Field name made lowercase.
    measurement_typeid = models.ForeignKey('TblLuMeasurementTypes', db_column='Measurement_TypeID')  # Field name made lowercase.
    measurement_unitid = models.ForeignKey('TblLuMeasurementUnits', db_column='Measurement_UnitID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
    replicates = models.IntegerField(db_column='Replicates')  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_BioRep_Image_Histology'


class TblBiorepImageSets(models.Model):
    biorepimagesetid = models.AutoField(db_column='BioRepImageSetID', primary_key=True)  # Field name made lowercase.
    image_setid = models.IntegerField(db_column='Image_SetID')  # Field name made lowercase.
    imageid = models.ForeignKey('TblHashBiorepImages', db_column='ImageID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_BioRep_Image_Sets'


class TblBioReplicates(models.Model):
    biorepid = models.AutoField(db_column='BioRepID', primary_key=True)  # Field name made lowercase.
    sampleid = models.ForeignKey('TblSamples', db_column='SampleID')  # Field name made lowercase.
    replicate = models.CharField(db_column='Replicate', max_length=50)  # Field name made lowercase.
    sample_typeid = models.ForeignKey('TblLuSampleTypes', db_column='Sample_TypeID')  # Field name made lowercase.
    mass_g = models.FloatField(db_column='Mass_g', blank=True, null=True)  # Field name made lowercase.
    redo = models.NullBooleanField(db_column='Redo')  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Bio_Replicates'


class TblCollections(models.Model):
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


class TblComments(models.Model):
    record_typeid = models.ForeignKey('TblLuRecordTypes', db_column='Record_TypeID')  # Field name made lowercase.
    foreign_key = models.AutoField(db_column='Foreign_Key')  # Field name made lowercase.
    comment_typeid = models.ForeignKey('TblLuCommentTypes', db_column='Comment_TypeID')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Comments'
        unique_together = (('Record_TypeID', 'Foreign_Key', 'Comment_TypeID'),)


class TblDevelopmentNotes(models.Model):
    key_word = models.CharField(db_column='Key_Word', primary_key=True, max_length=255)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=512)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Development_Notes'


class TblEnviroMeasurementDates(models.Model):
    enviro_dateid = models.AutoField(db_column='Enviro_DateID', primary_key=True)  # Field name made lowercase.
    record_typeid = models.ForeignKey('TblLuRecordTypes', db_column='Record_TypeID')  # Field name made lowercase.
    foreign_key = models.IntegerField(db_column='Foreign_Key')  # Field name made lowercase.
    sample_date = models.DateField(db_column='Sample_Date')  # Field name made lowercase.
    sample_time = models.TimeField(db_column='Sample_Time', blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Enviro_Measurement_Dates'
        unique_together = (('Record_TypeID', 'Foreign_Key', 'Sample_Date'),)


class TblEnviroMeasurements(models.Model):
    measurementid = models.AutoField(db_column='MeasurementID', primary_key=True)  # Field name made lowercase.
    enviro_dateid = models.ForeignKey(TblEnviroMeasurementDates, db_column='Enviro_DateID')  # Field name made lowercase.
    measurement_typeid = models.ForeignKey('TblLuMeasurementTypes', db_column='Measurement_TypeID')  # Field name made lowercase.
    measurement_unitid = models.ForeignKey('TblLuMeasurementUnits', db_column='Measurement_UnitID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
    replicates = models.IntegerField(db_column='Replicates')  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Enviro_Measurements'


class TblHashBiorepAssays(models.Model):
    biorepassayid = models.AutoField(db_column='BioRepAssayID', primary_key=True)  # Field name made lowercase.
    biorepprocessid = models.ForeignKey('TblHashBiorepProcess', db_column='BioRepProcessID')  # Field name made lowercase.
    assay_typeid = models.ForeignKey('TblLuAssayTypes', db_column='Assay_TypeID')  # Field name made lowercase.
    biomoleculeid = models.ForeignKey('TblLuBioMolecules', db_column='BioMoleculeID')  # Field name made lowercase.
    measurement_typeid = models.ForeignKey('TblLuMeasurementTypes', db_column='Measurement_TypeID')  # Field name made lowercase.
    measurement_unitid = models.ForeignKey('TblLuMeasurementUnits', db_column='Measurement_UnitID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    replicates = models.IntegerField(db_column='Replicates')  # Field name made lowercase.
    cv = models.FloatField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    redo = models.NullBooleanField(db_column='Redo')  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_BioRep_Assays'


class TblHashBiorepImages(models.Model):
    imageid = models.AutoField(db_column='ImageID', primary_key=True)  # Field name made lowercase.
    biorepprocessid = models.ForeignKey('TblHashBiorepProcess', db_column='BioRepProcessID')  # Field name made lowercase.
    image_label = models.CharField(db_column='Image_Label', max_length=50, blank=True, null=True)  # Field name made lowercase.
    slide_label = models.CharField(db_column='Slide_Label', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.
    link_to_image = models.CharField(db_column='Link_To_Image', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_BioRep_Images'
        unique_together = (('BioRepProcessID', 'Image_Label', 'Slide_Label'),)


class TblHashBiorepMorphology(models.Model):
    biorepmorphologyid = models.AutoField(db_column='BioRepMorphologyID', primary_key=True)  # Field name made lowercase.
    biorepprocessid = models.ForeignKey('TblHashBiorepProcess', db_column='BioRepProcessID')  # Field name made lowercase.
    measurement_typeid = models.ForeignKey('TblLuMeasurementTypes', db_column='Measurement_TypeID')  # Field name made lowercase.
    measurement_unitid = models.ForeignKey('TblLuMeasurementUnits', db_column='Measurement_UnitID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
    replicates = models.IntegerField(db_column='Replicates')  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_BioRep_Morphology'


class TblHashBiorepParasites(models.Model):
    biorepparasitesid = models.AutoField(db_column='BioRepParasitesID', primary_key=True)  # Field name made lowercase.
    biorepid = models.ForeignKey(TblBioReplicates, db_column='BioRepID')  # Field name made lowercase.
    speciesid = models.ForeignKey('TblLuSpecies', db_column='SpeciesID')  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    count_estimated = models.BooleanField(db_column='Count_Estimated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_BioRep_Parasites'


class TblHashBiorepProcess(models.Model):
    biorepid = models.ForeignKey(TblBioReplicates, db_column='BioRepID')  # Field name made lowercase.
    processid = models.ForeignKey('TblProcessing', db_column='ProcessID')  # Field name made lowercase.
    biorepprocessid = models.AutoField(db_column='BioRepProcessID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_BioRep_Process'
        unique_together = (('BioRepID', 'ProcessID'),)


class TblHashCollectionExperiments(models.Model):
    collectionid = models.ForeignKey(TblCollections, db_column='CollectionID')  # Field name made lowercase.
    experimentid = models.ForeignKey('TblLuExperiments', db_column='ExperimentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_Collection_Experiments'
        unique_together = (('CollectionID', 'ExperimentID'),)


class TblHashCollectionSpecies(models.Model):
    collectionid = models.ForeignKey(TblCollections, db_column='CollectionID')  # Field name made lowercase.
    speciesid = models.ForeignKey('TblLuSpecies', db_column='SpeciesID')  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=25, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    count_estimated = models.BooleanField(db_column='Count_Estimated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_Collection_Species'
        unique_together = (('CollectionID', 'SpeciesID'),)


class TblHashCollectionTraps(models.Model):
    colltrapid = models.AutoField(db_column='CollTrapID', primary_key=True)  # Field name made lowercase.
    collectionid = models.ForeignKey(TblCollections, db_column='CollectionID')  # Field name made lowercase.
    number_of_traps = models.IntegerField(db_column='Number_Of_Traps')  # Field name made lowercase.
    date_opened = models.DateField(db_column='Date_Opened')  # Field name made lowercase.
    time_opened = models.TimeField(db_column='Time_Opened')  # Field name made lowercase.
    date_closed = models.DateField(db_column='Date_Closed')  # Field name made lowercase.
    time_closed = models.TimeField(db_column='Time_Closed')  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_Collection_Traps'
        unique_together = (('CollectionID', 'Date_Opened', 'Time_Opened', 'Date_Closed', 'Time_Closed'),)


class TblHashPeopleSets(models.Model):
    peoplesetid = models.AutoField(db_column='PeopleSetID', primary_key=True)  # Field name made lowercase.
    record_typeid = models.ForeignKey('TblLuRecordTypes', db_column='Record_TypeID')  # Field name made lowercase.
    foreign_key = models.IntegerField(db_column='Foreign_Key')  # Field name made lowercase.
    personid = models.ForeignKey('TblLuPeople', db_column='PersonID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_People_Sets'


class TblHashTrapSpecies(models.Model):
    trapspeciesid = models.AutoField(db_column='TrapSpeciesID', primary_key=True)  # Field name made lowercase.
    colltrapid = models.ForeignKey(TblHashCollectionTraps, db_column='CollTrapID')  # Field name made lowercase.
    speciesid = models.ForeignKey('TblLuSpecies', db_column='SpeciesID')  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=25, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    count_estimated = models.BooleanField(db_column='Count_Estimated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_HASH_Trap_Species'


class TblLuAffiliations(models.Model):
    affiliationid = models.AutoField(db_column='AffiliationID', primary_key=True)  # Field name made lowercase.
    affiliation = models.CharField(db_column='Affiliation', max_length=100)  # Field name made lowercase.
    affiliation_code = models.CharField(db_column='Affiliation_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Affiliations'
        unique_together = (('Affiliation', 'Affiliation_Code'),)


class TblLuAssayTypes(models.Model):
    assay_typeid = models.AutoField(db_column='Assay_TypeID', primary_key=True)  # Field name made lowercase.
    assay_type = models.CharField(db_column='Assay_Type', max_length=100)  # Field name made lowercase.
    assay_type_code = models.CharField(db_column='Assay_Type_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    atype_short_description = models.CharField(db_column='AType_Short_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Assay_Types'
        unique_together = (('Assay_Type', 'Assay_Type_Code'),)


class TblLuBioMolecules(models.Model):
    biomoleculeid = models.AutoField(db_column='BioMoleculeID', primary_key=True)  # Field name made lowercase.
    biomolecule = models.CharField(db_column='BioMolecule', max_length=100)  # Field name made lowercase.
    biomolecule_code = models.CharField(db_column='BioMolecule_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    biomolecule_short_description = models.CharField(db_column='BioMolecule_Short_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Bio_Molecules'
        unique_together = (('BioMolecule', 'BioMolecule_Code'),)


class TblLuCollectionMethods(models.Model):
    collection_methodid = models.AutoField(db_column='Collection_MethodID', primary_key=True)  # Field name made lowercase.
    collection_method = models.CharField(db_column='Collection_Method', max_length=100)  # Field name made lowercase.
    collection_method_code = models.CharField(db_column='Collection_Method_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    collection_method_class = models.CharField(db_column='Collection_Method_Class', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Collection_Methods'
        unique_together = (('Collection_Method', 'Collection_Method_Code'),)


class TblLuCollectionTypes(models.Model):
    collection_typeid = models.AutoField(db_column='Collection_TypeID', primary_key=True)  # Field name made lowercase.
    collection_type = models.CharField(db_column='Collection_Type', max_length=100)  # Field name made lowercase.
    collection_type_code = models.CharField(db_column='Collection_Type_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Collection_Types'
        unique_together = (('Collection_Type', 'Collection_Type_Code'),)


class TblLuCommentTypes(models.Model):
    comment_typeid = models.AutoField(db_column='Comment_TypeID', primary_key=True)  # Field name made lowercase.
    comment_type = models.CharField(db_column='Comment_Type', max_length=100)  # Field name made lowercase.
    comment_type_code = models.CharField(db_column='Comment_Type_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Comment_Types'
        unique_together = (('Comment_Type', 'Comment_Type_Code'),)


class TblLuExperiments(models.Model):
    experimentid = models.AutoField(db_column='ExperimentID', primary_key=True)  # Field name made lowercase.
    experiment_name = models.CharField(db_column='Experiment_Name', max_length=150)  # Field name made lowercase.
    experiment_code = models.CharField(db_column='Experiment_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    experiment_short_description = models.CharField(db_column='Experiment_Short_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    link_to_protocol = models.CharField(db_column='Link_To_Protocol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey('TblLuRecordFlaws', db_column='FlawID', blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Experiments'
        unique_together = (('Experiment_Name', 'Experiment_Code'),)


class TblLuPeople(models.Model):
    peopleid = models.AutoField(db_column='PeopleID', primary_key=True)  # Field name made lowercase.
    affiliationid = models.ForeignKey(TblLuAffiliations, db_column='AffiliationID', blank=True, null=True)  # Field name made lowercase.
    job_title = models.CharField(db_column='Job_Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50)  # Field name made lowercase.
    middle_initial = models.CharField(db_column='Middle_Initial', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50)  # Field name made lowercase.
    principal_investigator = models.NullBooleanField(db_column='Principal_Investigator')  # Field name made lowercase.
    lab_tech = models.NullBooleanField(db_column='Lab_Tech')  # Field name made lowercase.
    consultant = models.NullBooleanField(db_column='Consultant')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state_province = models.CharField(db_column='State_Province', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='Postal_Code', max_length=25, blank=True, null=True)  # Field name made lowercase.
    emergency_contact_name = models.CharField(db_column='Emergency_Contact_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emergency_contact_phone = models.CharField(db_column='Emergency_Contact_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_People'
        unique_together = (('First_Name', 'Middle_Initial', 'Last_Name'),)


class TblLuProcessTypes(models.Model):
    process_typeid = models.AutoField(db_column='Process_TypeID', primary_key=True)  # Field name made lowercase.
    process_type = models.CharField(db_column='Process_Type', max_length=100)  # Field name made lowercase.
    process_type_code = models.CharField(db_column='Process_Type_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ptype_short_description = models.CharField(db_column='PType_Short_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Process_Types'
        unique_together = (('Process_Type', 'Process_Type_Code'),)


class TblLuReagents(models.Model):
    reagentid = models.AutoField(db_column='ReagentID', primary_key=True)  # Field name made lowercase.
    reagent = models.CharField(db_column='Reagent', max_length=100)  # Field name made lowercase.
    reagent_code = models.CharField(db_column='Reagent_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reagent_class = models.CharField(db_column='Reagent_Class', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Reagents'
        unique_together = (('Reagent', 'Reagent_Code'),)


class TblLuRecordFlaws(models.Model):
    flawid = models.AutoField(db_column='FlawID', primary_key=True)  # Field name made lowercase.
    record_typeid = models.ForeignKey('TblLuRecordTypes', db_column='Record_TypeID')  # Field name made lowercase.
    flaw = models.CharField(db_column='Flaw', max_length=200)  # Field name made lowercase.
    flaw_short_description = models.CharField(db_column='Flaw_Short_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Record_Flaws'
        unique_together = (('Record_TypeID', 'Flaw'),)


class TblLuRecordTypes(models.Model):
    record_typeid = models.AutoField(db_column='Record_TypeID', primary_key=True)  # Field name made lowercase.
    record_type = models.CharField(db_column='Record_Type', unique=True, max_length=50)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Record_Types'


class TblLuSampleTypes(models.Model):
    sample_typeid = models.AutoField(db_column='Sample_TypeID', primary_key=True)  # Field name made lowercase.
    sample_type = models.CharField(db_column='Sample_Type', max_length=100)  # Field name made lowercase.
    sample_type_code = models.CharField(db_column='Sample_Type_Code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stype_short_description = models.CharField(db_column='SType_Short_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Sample_Types'
        unique_together = (('Sample_Type', 'Sample_Type_Code'),)


class TblLuTreatmentTypes(models.Model):
    treatment_typeid = models.AutoField(db_column='Treatment_TypeID', primary_key=True)  # Field name made lowercase.
    experimentid = models.ForeignKey(TblLuExperiments, db_column='ExperimentID', blank=True, null=True)  # Field name made lowercase.
    treatment = models.CharField(db_column='Treatment', max_length=200)  # Field name made lowercase.
    treatment_code = models.CharField(db_column='Treatment_Code', max_length=25, blank=True, null=True)  # Field name made lowercase.
    treatment_type = models.CharField(db_column='Treatment_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    placement = models.CharField(db_column='Placement', max_length=25, blank=True, null=True)  # Field name made lowercase.
    treatment_short_description = models.CharField(db_column='Treatment_Short_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='Sort_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Treatment_Types'
        unique_together = (('ExperimentID', 'Treatment'),)


class TblLuUsers(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=100)  # Field name made lowercase.
    is_admin = models.BooleanField(db_column='Is_Admin')  # Field name made lowercase.
    password_hash = models.CharField(db_column='Password_Hash', max_length=128)  # Field name made lowercase.
    avatar_hash = models.CharField(db_column='Avatar_Hash', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_LU_Users'


class TblProcessing(models.Model):
    processid = models.AutoField(db_column='ProcessID', primary_key=True)  # Field name made lowercase.
    process_typeid = models.ForeignKey(TblLuProcessTypes, db_column='Process_TypeID')  # Field name made lowercase.
    containerid = models.ForeignKey(TblLuContainers, db_column='ContainerID')  # Field name made lowercase.
    container_label = models.CharField(db_column='Container_Label', max_length=50)  # Field name made lowercase.
    process_date = models.DateField(db_column='Process_Date', blank=True, null=True)  # Field name made lowercase.
    process_time = models.TimeField(db_column='Process_Time', blank=True, null=True)  # Field name made lowercase.
    reagentid = models.ForeignKey(TblLuReagents, db_column='ReagentID', blank=True, null=True)  # Field name made lowercase.
    reagent_volume = models.FloatField(db_column='Reagent_Volume', blank=True, null=True)  # Field name made lowercase.
    measurement_unitid = models.ForeignKey(TblLuMeasurementUnits, db_column='Measurement_UnitID', blank=True, null=True)  # Field name made lowercase.
    time_in_reagent = models.CharField(db_column='Time_in_Reagent', max_length=10, blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey(TblLuRecordFlaws, db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Processing'
        unique_together = (('Process_TypeID', 'ContainerID', 'Container_Label', 'Process_Date', 'Process_Time', 'ReagentID'),)


class TblSamples(models.Model):
    trrepid = models.ForeignKey('TblTreatmentReplicates', db_column='TrRepID')  # Field name made lowercase.
    sampleid = models.AutoField(db_column='SampleID', primary_key=True)  # Field name made lowercase.
    sample_date = models.DateField(db_column='Sample_Date')  # Field name made lowercase.
    sample_time = models.TimeField(db_column='Sample_Time', blank=True, null=True)  # Field name made lowercase.
    time_block = models.CharField(db_column='Time_Block', max_length=4, blank=True, null=True)  # Field name made lowercase.
    days_post_fertilization = models.IntegerField(db_column='Days_Post_Fertilization', blank=True, null=True)  # Field name made lowercase.
    sample_size = models.IntegerField(db_column='Sample_Size', blank=True, null=True)  # Field name made lowercase.
    mass_g = models.FloatField(db_column='Mass_g', blank=True, null=True)  # Field name made lowercase.
    flaw_temp = models.CharField(db_column='Flaw_Temp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey(TblLuRecordFlaws, db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Samples'
        unique_together = (('TrRepID', 'Sample_Date', 'Sample_Time', 'Time_Block'),)


class TblTreatmentReplicates(models.Model):
    treatmentid = models.ForeignKey('TblTreatments', db_column='TreatmentID')  # Field name made lowercase.
    trrepid = models.AutoField(db_column='TrRepID', primary_key=True)  # Field name made lowercase.
    replicate = models.CharField(db_column='Replicate', max_length=50)  # Field name made lowercase.
    setup_date = models.DateField(db_column='Setup_Date', blank=True, null=True)  # Field name made lowercase.
    setup_time = models.TimeField(db_column='Setup_Time', blank=True, null=True)  # Field name made lowercase.
    setup_sample_size = models.IntegerField(db_column='Setup_Sample_Size', blank=True, null=True)  # Field name made lowercase.
    mass_g = models.FloatField(db_column='Mass_g', blank=True, null=True)  # Field name made lowercase.
    flawid = models.ForeignKey(TblLuRecordFlaws, db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Treatment_Replicates'
        unique_together = (('TreatmentID', 'Replicate', 'Setup_Date', 'Setup_Time'),)


class TblTreatments(models.Model):
    treatmentid = models.AutoField(db_column='TreatmentID', primary_key=True)  # Field name made lowercase.
    treatment_typeid = models.ForeignKey(TblLuTreatmentTypes, db_column='Treatment_TypeID')  # Field name made lowercase.
    containerid = models.ForeignKey(TblLuContainers, db_column='ContainerID', blank=True, null=True)  # Field name made lowercase.
    study_locationid = models.ForeignKey(TblLuStudyLocations, db_column='Study_LocationID')  # Field name made lowercase.
    speciesid = models.ForeignKey(TblLuSpecies, db_column='SpeciesID')  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=25)  # Field name made lowercase.
    flawid = models.ForeignKey(TblLuRecordFlaws, db_column='FlawID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Treatments'
