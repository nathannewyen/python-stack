from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books),
    path('books/add/', views.add),
    path('books/add/process/', views.add_process),
    path('books/<int:id>/add/review/process/', views.add_review),
    path('books/<int:id>/', views.book_info),
    path('user/<int:id>/', views.user),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
