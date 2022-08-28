from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('support/', views.support),

    path('paypal/', views.paypal),
    path('contact/', views.contact),

    path('stripee/', views.stripee),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]