from django.db import models

from autoslug import AutoSlugField


class Species(models.Model):
    common_name = models.CharField(max_length=100)
    genus = models.CharField(max_length=50, blank=True)
    species = models.CharField(max_length=50, blank=True)
    parasite = models.BooleanField(default=False)
    sort_order = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='common_name')

    def __str__(self):
        return self.common_name

    class Meta:
        unique_together = ('common_name', 'species')
        ordering = ['sort_order']
        verbose_name_plural = 'species'
