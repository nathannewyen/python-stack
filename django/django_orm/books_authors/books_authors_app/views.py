from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.


def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books_info': all_books,
    }
    return render(request, 'index.html', context)


def books(request):
    return redirect('/')


def book_info(request, id):
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    for i in all_books:
        if id == i.id:
            authors_name = i.authors.all()

    context = {
        'all_authors': all_authors,
        'all_books': all_books,
        'id': id,
        'authors_name': authors_name,
    }
    return render(request, 'book_info.html', context)


def authors(request):
    all_authors = Author.objects.all()
    context = {
        'all_authors_info': all_authors
    }
    return render(request, 'authors.html', context)


def authors_info(request, id):
    all_books = Book.objects.all()
    all_authors = Author.objects.all()
    for i in all_authors:
        if id == i.id:
            books_name = i.books.all()
    context = {
        'all_books': all_books,
        'all_authors': all_authors,
        'id': id,
        'books_name': books_name,
    }
    return render(request, 'authors_info.html', context)


def add_book(request):
    if len(str(request.POST["title"])) < 2:
        print("Needs more the 2 characters to submit")
    else:
        print("Meets rule")
        print(request.POST["desc"])

        Book.objects.create(
            title=request.POST["title"], desc=request.POST["desc"])
    return redirect('/')


def add_author(request):
    if len(str(request.POST["first_name"])) < 2:
        print("Needs more the 2 characters to submit")
    else:
        Author.objects.create(
            first_name=request.POST["first_name"], last_name=request.POST["last_name"],
            notes=request.POST["notes"])
    return redirect('/authors')


def book_to_author(request, bookid):
    this_author = Author.objects.get(id=request.POST['author'])
    this_book = Book.objects.get(id=bookid)
    this_book.authors.add(this_author)
    return redirect(f"/books/{bookid}")


def author_to_book(request, authorid):
    this_book = Book.objects.get(id=request.POST['book'])
    this_author = Author.objects.get(id=authorid)
    this_author.books.add(this_book)
    return redirect(f"/authors/{authorid}")
