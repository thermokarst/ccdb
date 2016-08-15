from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


if settings.DEBUG:
    from debug_toolbar.middleware import DebugToolbarMiddleware

    class PatchedDebugToolbarMiddleware(MiddlewareMixin,
                                        DebugToolbarMiddleware):
        pass
