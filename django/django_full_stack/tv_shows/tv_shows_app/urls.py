from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/', views.all_show_info),
    path('shows/<int:id>', views.single_show_info),
    path('shows/new/', views.new_show),
    path('shows/<int:id>/edit', views.show_edit),
    path('shows/create/', views.create),
    path('shows/<int:id>/update', views.update),
    path('shows/<int:id>/destroy', views.delete),
    path('shows/validate_title/', views.validate_title, name='validate_title'),
]
