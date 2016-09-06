from django.db import models

from rest_framework.reverse import reverse


class AdminSection(models.Model):
    name = models.CharField(max_length=255)
    sort = models.IntegerField()

    def __str__(self):
        return self.name


class AdminEntry(models.Model):
    package = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    section = models.ForeignKey(AdminSection)
    sort = models.IntegerField()

    def admin_url(self, request=None):
        lookup = 'admin:{}_{}_changelist'.format(self.package, self.model)
        relative = reverse(lookup)
        return request.build_absolute_uri(relative)

    def __str__(self):
        return "%s %s" % (self.package, self.model)
