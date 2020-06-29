from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout/', views.checkout),
    path('checkout/process/', views.checkout_process)
]
