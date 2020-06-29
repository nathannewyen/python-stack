from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books),
    path('books/process/', views.add_book),
    path('books/<int:id>/', views.book_info),
    path('books/<int:id>/update/', views.update),
    path('books/<int:id>/like/', views.like),
    path('books/<int:id>/dislike/', views.dislike),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('books/<int:id>/delete/', views.delete),
    path('user/<int:id>/', views.user)
]
