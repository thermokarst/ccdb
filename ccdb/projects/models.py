from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from autoslug import AutoSlugField


class Project(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True)
    iacuc_number = models.CharField(max_length=25, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['sort_order']


class Grant(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=255, blank=True)
    projects = models.ManyToManyField(Project, related_name='grants')
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'code',)
        ordering = ['sort_order']
