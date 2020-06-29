from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.process_money),
    path('increase', views.increase_money),
    path('decrease', views.decrease_money)
]
