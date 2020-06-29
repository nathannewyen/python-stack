from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('timedisplay', views.timedisplay)
]
