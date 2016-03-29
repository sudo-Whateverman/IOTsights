from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shots_list, name='shots_list'),
    url(r'^map/', views.shots_map, name='shots_map'),
    url(r'^add/', views.shot_new, name='add')
]