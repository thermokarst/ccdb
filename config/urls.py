from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from django.views import defaults as default_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/', include('ccdb.api.urls', namespace='api')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index'), permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]
