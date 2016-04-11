from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shots_list, name='shots_list'),
    url(r'^map/', views.shots_map, name='shots_map'),
    url(r'^add/', views.shot_new, name='add'),
    url(
        r'^get/(?P<iot_id>[0-9]+)/(?P<lat>[0-9]+)/(?P<longt>[0-9]+)/(?P<elev>[0-9]+)/(?P<head>[0-9]+)$',
        views.shot_new_get, name='add_get'),
]
