from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import re
import bcrypt


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}

        # Check Name
        if len(postData["name"]) == 0:
            errors["name_error"] = "Please enter your name!"
        elif len(postData["name"]) < 3:
            errors["name_error"] = "Your Name is too short"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["name"]):
            errors["name_error"] = "Invalid name"

        # Check Alias
        if len(postData["alias"]) == 0:
            errors["alias_error"] = "Please enter your alias!"
        elif len(postData["alias"]) < 2:
            errors["alias_error"] = "Your alias is too short!"

        # Check email
        emailMatch = Users.objects.filter(email=postData["reg_email"])
        if len(emailMatch) > 0:
            errors["reg_email_error"] = "This email is already taken"

        elif len(postData["reg_email"]) < 1:
            errors["reg_email_error"] = "Email should longer"

        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["reg_email"]):
            errors["reg_email_error"] = "Please enter valid email form (eg. abc123@gmail.com)"

        # Check Password
        if len(postData["reg_password"]) < 1:
            errors["reg_password_error"] = "Please enter your password"
        elif len(postData["reg_password"]) and len(postData["confirm-password"]) < 8:
            errors["reg_password_error"] = "Please enter your password more than 8 characters"
        elif postData["reg_password"] != postData["confirm-password"]:
            errors["reg_password_error"] = "Confirm password must match with your password"

        return errors

    # Check login
    def login_validator(self, postData):
        errors = {}

        # Check email
        if len(postData["login_email"]) == 0:
            errors["login_email_error"] = "Please enter your email"
        elif len(postData["login_email"]) < 3:
            errors["login_email_error"] = "Your email is too short"

        # Check password
        if len(postData["login_password"]) == 0:
            errors["login_password_error"] = "Please enter your password"
        elif len(postData["login_password"]) < 2:
            errors["login_password_error"] = "Your password is invalid"

        # email must be found in the database, in order to log in
        emailExist = Users.objects.filter(
            email=postData['login_email'])
        if len(emailExist) == 0:
            errors['login_email_error'] = "This email was not found. Please register first."
        else:
            email = emailExist[0]
            # if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(postData['login_password'].encode(), email.password.encode()):
                errors['login_password_error'] = "Password does not match"

        return errors


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}

        if len(postData["title"]) == 0:
            errors['title_error'] = "Please enter your title"
        elif len(postData["title"]) < 3:
            errors["title_error"] = "Your title is too short"
        elif len(Book.objects.filter(title=postData["title"])) > 0:
            errors["title_error"] = "This title is already existed"

        return errors


class Users(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


class Review(models.Model):
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    review = models.TextField()
    user = models.ForeignKey(
        Users, related_name='user_reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name='book_reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='authors')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
