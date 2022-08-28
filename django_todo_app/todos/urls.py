from django.urls import re_path
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<id>/',views.details),
    path('add/',views.add, name='add'),
]
