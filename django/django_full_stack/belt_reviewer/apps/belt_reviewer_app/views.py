from django.shortcuts import render, redirect
from .models import Users, Book, Review, Author
from django.contrib import messages
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'index.html')


def books(request):
    context = {
        'user': Users.objects.get(id=request.session["user_id"]),
        'books': Book.objects.all(),
        'reviews': Review.objects.all()
    }
    return render(request, 'books.html', context)


def add(request):
    context = {
        'user': Users.objects.get(id=request.session["user_id"]),
        'authors': Author.objects.all(),
    }
    return render(request, 'add_book.html', context)


def add_process(request):
    user = Users.objects.get(id=request.session["user_id"])
    errors = Book.objects.book_validator(request.POST)

    # Check Valid Register
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/books/add/")

    else:
        book = Book.objects.create(title=request.POST["title"])

        # New Author
        if request.POST["new_author"] != u"":

            # If new author doesn't exist - create new author
            if len(Author.objects.filter(name=request.POST["new_author"])) < 1:
                author = Author.objects.create(name=request.POST["new_author"])
                author.books.add(book)
                author.save()

            # If author already exists - use author already have
            else:
                author = Author.objects.get(name=request.POST["new_author"])
                author.books.add(book)
                author.save()

        else:
            author = Author.objects.get(name=request.POST["exist_author"])
            author.books.add(book)
            author.save()

        # Create Review
        review = Review.objects.create(
            rating=request.POST["rating"], review=request.POST["review"], user=user, book=book)

        return redirect("/books/")


def book_info(request, id):
    context = {
        'user': Users.objects.get(id=request.session["user_id"]),
        'book': Book.objects.get(id=id),
        "book_authors": Book.objects.get(id=id).authors.all(),
        "reviews": Review.objects.filter(book=Book.objects.get(id=id)).order_by("-created_at"),

    }

    return render(request, 'book_info.html', context)


def add_review(request, id):
    user = Users.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=id)
    Review.objects.create(
        review=request.POST["review"], rating=request.POST["rating"], user=user, book=book)
    return redirect(f"/books/{book.id}/")


def user(request, id):
    context = {
        "total_review": Users.objects.get(id=id).user_reviews.all().count(),
        'user': Users.objects.get(id=id),
        "reviews": Users.objects.get(id=id).user_reviews.all(),
    }
    return render(request, 'user_info.html', context)


def register(request):
    errors = Users.objects.register_validator(request.POST)

    # Check Valid Register
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    # Create User
    else:
        hashed_pw = bcrypt.hashpw(request.POST["reg_password"].encode(
            "utf-8"), bcrypt.gensalt()).decode()
        user = Users.objects.create(
            name=request.POST["name"],
            alias=request.POST["alias"],
            email=request.POST["reg_email"],
            password=hashed_pw
        )
        request.session["user_id"] = user.id
        return redirect(f"/user/{user.id}")


def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    else:
        user = Users.objects.filter(email=request.POST["login_email"])
        logged_user = user[0]
        request.session["user_id"] = logged_user.id
        return redirect("/books/")

    return redirect(f"/user/{user.id}")


def logout(request):
    request.session.clear()
    return redirect("/")
