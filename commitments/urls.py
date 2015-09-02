#URLS for the commitments app

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from commitments import views

urlpatterns = [
    url(r'^profile/$', views.commitment_profile)
]

urlpatterns = format_suffix_patterns(urlpatterns)
