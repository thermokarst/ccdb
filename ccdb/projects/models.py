from django.db import models

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


class GrantReport(models.Model):
    grant = models.ForeignKey(Grant, related_name='reports')
    title = models.CharField(max_length=200)
    report_type = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    due_date = models.DateField(blank=True, null=True)
    submitted_date = models.DateField(blank=True, null=True)
    attachment = models.FileField(
        upload_to='projects/grants/grant_report_attachments/%Y/%m/%d',
        blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('grant', 'title', 'due_date',)
        ordering = ['sort_order']
