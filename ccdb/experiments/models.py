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
