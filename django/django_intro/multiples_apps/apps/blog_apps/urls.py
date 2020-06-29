from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/new', views.news),
    path('/create', views.create),
    path('/show', views.show),
    path('/show/<number>/', views.show),
    path('/show/<number>/edit', views.edit),
    path('/show/<number>/delete', views.destroy),

]
