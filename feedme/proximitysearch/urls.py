__author__ = 'oahayder'

from django.conf.urls import patterns, url, include
from proximitysearch import views

urlpatterns = patterns('',
    # ex: /proximitysearch/nearby/35.5555/120.99999
    url(r'^nearby/(?P<latitude>\-?\d+\.?\d*)/(?P<longitude>\-?\d+\.?\d*)/$', views.NearbyFoodFacilityList.as_view(), name='nearby'),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
)
