from django.conf.urls import url, include

from rest_framework import routers

from . import views as api_v


router = routers.DefaultRouter()

router.register(r'administrative-urls', api_v.AdminURLs, base_name='adminurls')

urlpatterns = [
    url(r'^auth/login/', api_v.Login.as_view()),
    url(r'^auth/password/reset/confirm/',
        api_v.PasswordResetConfirm.as_view()),
    url(r'^auth/password/reset/', api_v.PasswordReset.as_view()),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^v1/', include(router.urls, namespace='v1')),
]
