from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('accounts.urls', namespace='accounts')),
    url(r'^api/', include('commitments.urls', namespace='commitments')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
