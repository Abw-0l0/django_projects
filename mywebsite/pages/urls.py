from django.urls import path

from . import views

urlpatterns = [
    path('polling/', views.index, name='polling'),
]
