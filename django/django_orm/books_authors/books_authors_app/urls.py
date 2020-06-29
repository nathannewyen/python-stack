from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books),
    path('books/<int:id>/', views.book_info),
    path('authors/', views.authors),
    path('authors/<int:id>/', views.authors_info),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('book_to_author/<bookid>', views.book_to_author),
    path('author_to_book/<authorid>', views.author_to_book)
]
