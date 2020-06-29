from django.db import models
import re
import bcrypt

# Create your models here.


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}

        # Check Name
        if len(postData["fname"]) == 0:
            errors["fname_error"] = "Please enter your First Name!"
        elif len(postData["fname"]) < 3:
            errors["fname_error"] = "Your First Name is too short"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["fname"]):
            errors["fname_error"] = "Invalid first name"

        if len(postData["lname"]) == 0:
            errors["lname_error"] = "Please enter your Last Name!"
        elif len(postData["lname"]) < 3:
            errors["lname_error"] = "Your Last Name is too short"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["lname"]):
            errors["lname_error"] = "Invalid last name"

        # Check Username
        if len(postData["reg_email"]) == 0:
            errors["reg_email_error"] = "Please enter your username!"
        if len(postData["reg_email"]) < 3:
            errors["reg_email_error"] = "Your username is too short!"

        # Check Password
        if len(postData["reg_password"]) < 1:
            errors["reg_password_error"] = "Please enter your password"
        elif len(postData["reg_password"]) and len(postData["confirm-password"]) < 8:
            errors["reg_password_error"] = "Please enter your password more than 8 characters"
        elif postData["reg_password"] != postData["confirm-password"]:
            errors["confirm_password_error"] = "Confirm password must match with your password"

        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emailExist = User.objects.filter(email=postData["login_email"])
        # Check email
        if len(postData["login_email"]) == 0:
            errors["login_email_error"] = "Please enter your email"
        elif len(postData["login_email"]) < 2:
            errors["login_email_error"] = "Your email is invalid"
        elif not EMAIL_REGEX.match(postData['login_email']):
            errors["login_email_error"] = "Your email is invalid"

        # Check password
        if len(postData["login_password"]) == 0:
            errors["login_password_error"] = "Please enter your password"
        elif len(postData["login_password"]) < 2:
            errors["login_password_error"] = "Your password is invalid"

        # email must be found in the database, in order to log in
        emailsExist = User.objects.filter(email=postData['login_email'])
        if len(emailsExist) == 0:
            errors['login_email_error'] = "This email was not found. Please register first."
        else:
            user = emailsExist[0]
            # if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
                errors['login_password_error'] = "Password does not match"

        return errors


class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData["title"]) == 0:
            errors["title_error"] = "Title cannot be empty"
        elif len(postData["title"]) < 3:
            errors["title_error"] = "Title is too short"

        if len(postData["description"]) == 0:
            errors["description_error"] = "Description cannot be empty"
        elif len(postData["description"]) < 5:
            errors["description_error"] = "Description is at least 5 characters"

        return errors


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User,
                                    related_name="book_uploaded", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


class Like(models.Model):
    u_like = models.ForeignKey(
        User, related_name="user_like", on_delete=models.CASCADE)
    b_like = models.ForeignKey(
        Book, related_name="book_like", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
