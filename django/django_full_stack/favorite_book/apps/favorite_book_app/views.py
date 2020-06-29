from django.shortcuts import render, redirect
from .models import User, Book, Like
from django.contrib import messages
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'index.html')


def books(request):

    context = {
        'user': User.objects.get(id=request.session["user_id"]),
        'all_books': Book.objects.all(),
    }

    return render(request, 'books.html', context)


def book_info(request, id):

    user_who_like = Book.objects.get(id=id).book_like.all()
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])

    context = {
        'book': Book.objects.get(id=id),
        'user': User.objects.get(id=request.session["user_id"]),
        'user_who_like': Book.objects.get(id=id).book_like.all(),
    }
    return render(request, 'book_info.html', context)


def register(request):
    errors = User.objects.register_validator(request.POST)

    # Check valid registration
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    else:
        hashed_pw = bcrypt.hashpw(
            request.POST["reg_password"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(fname=request.POST["fname"],
                                   lname=request.POST["lname"],
                                   email=request.POST["reg_email"],
                                   password=hashed_pw
                                   )
        request.session["user_id"] = user.id
        return redirect("/books/")


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else:
        user = User.objects.filter(email=request.POST["login_email"],)
        logged_user = user[0]
        request.session["user_id"] = logged_user.id
        request.session['loggedin'] = True
        return redirect("/books/")


def logout(request):
    request.session.clear()
    return redirect("/")


def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/books/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        book = Book.objects.create(
            title=request.POST["title"], description=request.POST["description"], uploaded_by=user)
        like = Like.objects.create(u_like=user, b_like=book)

    return redirect(f"/books/{book.id}")


def update(request, id):
    book = Book.objects.get(id=id)
    book.description = request.POST["description"]
    book.save()
    return redirect("/books/")


def like(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])
    like = Like.objects.get_or_create(u_like=user, b_like=book)

    if not like[1]:
        messages.error(request, "Already added to favorite",
                       extra_tags="like_error")
        return redirect("/books/")

    context = {
        'book_user_like': User.objects.get(id=request.session["user_id"]).user_like.all(),
        'book': Book.objects.get(id=id),
        'like1': like[1],
    }

    return redirect(f"/books/{book.id}", context)


def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/books/")


def dislike(request, id):
    book = Book.objects.get(id=id)
    book_user_like = User.objects.get(
        id=request.session["user_id"]).user_like.all()

    for i in book_user_like:
        if i.b_like.id == book.id:
            i.delete()
    return redirect(f"/books/{book.id}")


def user(request, id):

    context = {
        'book_user_like': User.objects.get(id=request.session["user_id"]).user_like.all(),
        'user': User.objects.get(id=id)
    }

    return render(request, 'user.html', context)
