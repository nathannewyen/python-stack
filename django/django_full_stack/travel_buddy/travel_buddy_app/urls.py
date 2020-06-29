from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('travels/', views.user),
    path('travels/destination/<int:id>/', views.destination),
    path('travels/add/', views.add_trip),
    path('travels/add/process/', views.add_trip_process),
    path('travels/join/<int:id>/', views.join),
    path('travels/delete/<int:id>', views.delete),
]
