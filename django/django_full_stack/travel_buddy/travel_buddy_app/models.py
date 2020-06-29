from django.db import models
import re
import bcrypt
import datetime
# Create your models here.


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}

        # Check Name
        if len(postData["fname"]) == 0:
            errors["fname_error"] = "Please enter your name!"
        elif len(postData["fname"]) < 3:
            errors["fname_error"] = "Your Name is too short"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["fname"]):
            errors["fname_error"] = "Invalid last name"

        # Check Username
        if len(postData["username"]) == 0:
            errors["username_error"] = "Please enter your username!"
        if len(postData["username"]) < 3:
            errors["username_error"] = "Your username is too short!"

        # Check Password
        if len(postData["password"]) < 1:
            errors["password_error"] = "Please enter your password"
        elif len(postData["password"]) and len(postData["confirm-password"]) < 8:
            errors["password_error"] = "Please enter your password more than 8 characters"
        elif postData["password"] != postData["confirm-password"]:
            errors["password_error"] = "Confirm password must match with your password"

        return errors

    def login_validator(self, postData):
        errors = {}
        # Check username
        if len(postData["login_username"]) == 0:
            errors["login_username_error"] = "Please enter your username"
        elif len(postData["login_username"]) < 3:
            errors["login_username_error"] = "Your username is too short"

        # Check password
        if len(postData["login_password"]) == 0:
            errors["login_password_error"] = "Please enter your password"
        elif len(postData["login_password"]) < 2:
            errors["login_password_error"] = "Your password is invalid"

        # email must be found in the database, in order to log in
        usernameExist = User.objects.filter(
            username=postData['login_username'])
        if len(usernameExist) == 0:
            errors['login_username_error'] = "This username was not found. Please register first."
        else:
            user = usernameExist[0]
            # if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
                errors['login_password_error'] = "Password does not match"

        return errors


class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}

        if len(postData["destination"]) == 0:
            errors["destination_error"] = "Please enter your destination"
        if len(postData["description"]) < 5:
            errors["description_error"] = "Description should longer than 5 characters"

        if len(postData["from"]) == 0:
            errors["travel_from_error"] = "Please enter your date you want to plan. It cannot be empty"
        elif postData["from"] < str(datetime.date.today()):
            errors["travel_from_error"] = "Date plan to travel can't be the past. Only in future"
        elif postData["to"] < postData["from"]:
            errors["travel_to_error"] = "Date travel to should be in the future"

        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.TextField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField()
    plan_by = models.ForeignKey(
        User, related_name="user_plan", on_delete=models.CASCADE)
    join = models.ManyToManyField(User, related_name="user_join")
    travel_from = models.DateField()
    travel_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
