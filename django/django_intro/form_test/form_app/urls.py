from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('user', views.create_user),
    path('success', views.success)
]
