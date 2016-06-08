from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

import pytz


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    timezone = models.CharField(_("Current Timezone"), max_length=255,
                                default="UTC",
                                choices=[(x, x) for x in pytz.common_timezones],
                                blank=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
