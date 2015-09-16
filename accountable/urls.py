from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('accounts.urls', namespace='accounts')),
    url(r'^api/v1/', include('commitments.urls', namespace='commitments')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
