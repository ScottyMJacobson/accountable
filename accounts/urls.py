from django.conf.urls import patterns, url, include
from accounts import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'accounts', views.UserView, 'list')


urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
