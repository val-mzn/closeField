from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('farms', views.farm_list, name='farm_list'),
    path('map', views.map, name='map'),
]