import pytz

from django.utils import timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        if not request.user.is_anonymous():
            tzname = request.user.timezone
            if tzname:
                timezone.activate(pytz.timezone(tzname))
            else:
                timezone.deactivate()
