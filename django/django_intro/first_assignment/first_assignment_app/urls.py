from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<numDivs>', views.createDivs),
    path('<numDivs>/edit', views.edit),
    path('<numDivs>/delete', views.delete)
]
