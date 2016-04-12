from django.conf.urls import url
from . import views

re_ = "(-?\d+(?:\.\d+)?)"

urlpatterns = [
    url(r'^$', views.shots_list, name='shots_list'),
    url(r'^map/', views.shots_map, name='shots_map'),
    url(r'^add/', views.shot_new, name='add'),
    url(
        r'^get/(?P<iot_id>'+re_+')/(?P<lat>'+re_+')/(?P<longt>'+re_+')/(?P<elev>'+re_+')/(?P<head>'+re_+')$',
        views.shot_new_get, name='add_get'),
]
