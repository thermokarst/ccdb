from django.db import models

from autoslug import AutoSlugField


class Flaw(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']


class Experiment(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=255, blank=True)
    flaw = models.ForeignKey(Flaw, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')
    collections = models.ManyToManyField('collections_ccdb.Collection')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class ProtocolAttachment(models.Model):
    experiment = models.ForeignKey(Experiment)
    protocol = models.FileField(upload_to='experiments/protocols/%Y/%m/%d')

    def __str__(self):
        return self.protocol


class TreatmentType(models.Model):
    experiment = models.ForeignKey(Experiment, blank=True, null=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=25, blank=True)
    treatment_type = models.CharField(max_length=50, blank=True)
    placement = models.CharField(max_length=25, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return "{} {} {} {}".format(self.experiment, self.name,
                                    self.treatment_type, self.placement)

    class Meta:
        unique_together = ('experiment', 'name')
        ordering = ['sort_order']


class Treatment(models.Model):
    treatment_type = models.ForeignKey(TreatmentType)
    container = models.ForeignKey('misc.Container', blank=True, null=True)
    study_location = models.ForeignKey('locations.StudyLocation')
    species = models.ForeignKey('species.Species')
    sex = models.CharField(max_length=25)
    flaw = models.ForeignKey(Flaw, blank=True, null=True)
    display_name = models.CharField(max_length=255, editable=False)

    def save(self, *args, **kwargs):
        self.display_name = "{}_{}_{}_{}".format(self.treatment_type,
                                                 self.study_location, self.species,
                                                 self.sex)
        super(Treatment, self).save(*args, **kwargs)

    def __str__(self):
        return self.display_name


class TreatmentReplicate(models.Model):
    treatment = models.ForeignKey(Treatment)
    name = models.CharField(max_length=50)
    setup_date = models.DateField(blank=True, null=True)
    setup_time = models.TimeField(blank=True, null=True)
    setup_sample_size = models.IntegerField(blank=True, null=True)
    mass_g = models.FloatField(blank=True, null=True)
    flaw = models.ForeignKey(Flaw, blank=True, null=True)
    display_name = models.CharField(max_length=255, editable=False)

    def save(self, *args, **kwargs):
        self.display_name = "{}_{}_{}_{}".format(self.treatment,
                                                 self.setup_date, self.name,
                                                 self.setup_sample_size)
        super(TreatmentReplicate, self).save(*args, **kwargs)

    def __str__(self):
        return self.display_name

    class Meta:
        unique_together = ('treatment', 'name', 'setup_date', 'setup_time')


class AliveDeadCount(models.Model):
    treatment_replicate = models.ForeignKey(TreatmentReplicate)
    status_date = models.DateField()
    status_time = models.TimeField(blank=True, null=True)
    count_alive = models.IntegerField(blank=True, null=True)
    count_dead = models.IntegerField(blank=True, null=True)
    flaw = models.ForeignKey(Flaw, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.status_date)

    class Meta:
        verbose_name = 'Alive-dead Count'
