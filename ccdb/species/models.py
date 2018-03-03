from django.db import models


class Species(models.Model):
    common_name = models.CharField(max_length=100)
    genus = models.CharField(max_length=50, blank=True)
    species = models.CharField(max_length=50, blank=True)
    parasite = models.BooleanField(default=False)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.common_name

    class Meta:
        unique_together = ('common_name', 'species')
        ordering = ['sort_order']
        verbose_name_plural = 'species'


class Sex(models.Model):
    name = models.CharField(max_length=25, unique=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort_order']
        verbose_name_plural = 'sex'


class TrapSpecies(models.Model):
    collection_trap = models.ForeignKey('collections_ccdb.CollectionTrap',
                                        related_name='trap_species',
                                        on_delete=models.CASCADE)
    species = models.ForeignKey(Species, related_name='trap_species',
                                on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, related_name='trap_species',
                            on_delete=models.CASCADE, null=True)
    count = models.IntegerField(blank=True, null=True)
    count_estimated = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.collection_trap, self.species)

    class Meta:
        verbose_name_plural = 'trap-species'


class CollectionSpecies(models.Model):
    collection = models.ForeignKey('collections_ccdb.Collection',
                                   related_name='collection_species',
                                   on_delete=models.CASCADE)
    species = models.ForeignKey(Species, related_name='collection_species',
                                on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, related_name='collection_species',
                            on_delete=models.CASCADE, null=True)
    count = models.IntegerField(blank=True, null=True)
    count_estimated = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.collection, self.species)

    class Meta:
        unique_together = ('collection', 'species')
        verbose_name_plural = 'collection-species'
