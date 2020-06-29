from django.db import models
from django.utils import timezone
import re
import bcrypt
import math

# Create your models here.


class AdminManager(models.Manager):
    def register_admin_validators(self, postData):
        errors = {}

        # Check Name
        if len(postData["first_name_admin"]) == 0:
            errors["first_name_admin_error"] = "Please enter your first name!"
        elif len(postData["first_name_admin"]) < 3:
            errors["first_name_admin_error"] = "Your first name is too short"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["first_name_admin"]):
            errors["first_name_admin_error"] = "Invalid name"

        # Check Alias
        if len(postData["last_name_admin"]) == 0:
            errors["last_name_admin_error"] = "Please enter your last name!"
        elif len(postData["last_name_admin"]) < 2:
            errors["last_name_admin_error"] = "Your last name is too short!"

        # Check email
        emailMatch = Admin.objects.filter(email=postData["reg_email_admin"])
        if len(emailMatch) > 0:
            errors["reg_email_admin_error"] = "This email is already taken"

        elif len(postData["reg_email_admin"]) < 1:
            errors["reg_email_admin_error"] = "Email should longer"

        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["reg_email_admin"]):
            errors["reg_email_admin_error"] = "Please enter valid email form (eg. abc123@gmail.com)"

        # Check Password
        if len(postData["reg_password_admin"]) < 1:
            errors["reg_password_admin_error"] = "Please enter your password"
        elif len(postData["reg_password_admin"]) and len(postData["confirm_password_admin"]) < 8:
            errors["reg_password_admin_error"] = "Please enter your password more than 8 characters"
        elif postData["reg_password_admin"] != postData["confirm_password_admin"]:
            errors["reg_password_admin_error"] = "Confirm password must match with your password"

        return errors

    def login_admin_validator(self, postData):
        errors = {}

        # Check email
        if len(postData["login_email_admin"]) == 0:
            errors["login_email_admin_error"] = "Please enter your email"
        elif len(postData["login_email_admin"]) < 3:
            errors["login_email_admin_error"] = "Your email is too short"

        # Check password
        if len(postData["login_password_admin"]) == 0:
            errors["login_password_admin_error"] = "Please enter your password"
        elif len(postData["login_password_admin"]) < 2:
            errors["login_password_admin_error"] = "Your password is invalid"

        # email must be found in the database, in order to log in
        emailExist = Admin.objects.filter(
            email=postData['login_email_admin'])
        if len(emailExist) == 0:
            errors['login_email_admin_error'] = "This email was not found. Please register first."
        else:
            email = emailExist[0]
            # if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(postData['login_password_admin'].encode(), email.password.encode()):
                errors['login_password_admin_error'] = "Password does not match"

        return errors


class UserManager(models.Manager):
    def create_user_validators(self, postData):
        errors = {}

        # Check Name
        if len(postData["first_name"]) == 0:
            errors["first_name_error"] = "Please enter your first name!"
        elif len(postData["first_name"]) < 3:
            errors["first_name_error"] = "Your first name is too short"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["first_name"]):
            errors["first_name_error"] = "Invalid name"

        # Check Alias
        if len(postData["last_name"]) == 0:
            errors["last_name_error"] = "Please enter your last name!"
        elif len(postData["last_name"]) < 2:
            errors["last_name_error"] = "Your last name is too short!"

        # Check email
        emailMatch = User.objects.filter(email=postData["reg_email"])
        if len(emailMatch) > 0:
            errors["reg_email_error"] = "This email is already taken"

        elif len(postData["reg_email"]) < 1:
            errors["reg_email_error"] = "Email should longer"

        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["reg_email"]):
            errors["reg_email_error"] = "Please enter valid email form (eg. abc123@gmail.com)"

        # Check Password
        if len(postData["reg_password"]) < 1:
            errors["reg_password_error"] = "Please enter your password"
        elif len(postData["reg_password"]) and len(postData["confirm_password"]) < 8:
            errors["reg_password_error"] = "Please enter your password more than 8 characters"
        elif postData["reg_password"] != postData["confirm_password"]:
            errors["reg_password_error"] = "Confirm password must match with your password"

        return errors

    def add_user_validator(self, postData):
        errors = {}

        # Check Name
        if len(postData["first_name_user"]) == 0:
            errors["first_name_user_error"] = "Please enter your first name!"
        elif len(postData["first_name_user"]) < 3:
            errors["first_name_user_error"] = "Your first name is too short"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["first_name_user"]):
            errors["first_name_user_error"] = "Invalid name"

        # Check Alias
        if len(postData["last_name_user"]) == 0:
            errors["last_name_user_error"] = "Please enter your last name!"
        elif len(postData["last_name_user"]) < 2:
            errors["last_name_user_error"] = "Your last name is too short!"

        # Check email
        emailMatch = User.objects.filter(email=postData["reg_email_user"])
        if len(emailMatch) > 0:
            errors["reg_email_user_error"] = "This email is already taken"

        elif len(postData["reg_email_user"]) < 1:
            errors["reg_email_user_error"] = "Email should longer"

        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["reg_email_user"]):
            errors["reg_email_user_error"] = "Please enter valid email form (eg. abc123@gmail.com)"

        # Check Password
        if len(postData["reg_password_user"]) < 1:
            errors["reg_password_user_error"] = "Please enter your password"
        elif len(postData["reg_password_user"]) and len(postData["confirm_password_user"]) < 8:
            errors["reg_password_user_error"] = "Please enter your password more than 8 characters"
        elif postData["reg_password_user"] != postData["confirm_password_user"]:
            errors["reg_password_user_error"] = "Confirm password must match with your password"

        return errors

    def login_users_valid(self, postData):
        errors = {}

        # Check email
        if len(postData["login_email_user"]) == 0:
            errors["login_email_user_error"] = "Please enter your email"
        elif len(postData["login_email_user"]) < 3:
            errors["login_email_user_error"] = "Your email is too short"

        # Check password
        if len(postData["login_password_user"]) == 0:
            errors["login_password_user_error"] = "Please enter your password"
        elif len(postData["login_password_user"]) < 2:
            errors["login_password_user_error"] = "Your password is invalid"

        # email must be found in the database, in order to log in
        emailExist = User.objects.filter(
            email=postData['login_email_user'])
        if len(emailExist) == 0:
            errors['login_email_user_error'] = "This email was not found. Please register first."
        else:
            email = emailExist[0]
            # if email submitted in form is found in db, then password must match for that user with that email

            if not bcrypt.checkpw(postData['login_password_user'].encode(), email.password.encode()):
                errors['login_password_user_error'] = "Password does not match"

        return errors

    def users_update_valid(self, postData):
        errors = {}

        if len(postData["user_update_password"]) < 1:
            errors["user_update_password_error"] = "Please enter your password"
        elif len(postData["user_update_password"]) and len(postData["user_update_confirm_password"]) < 8:
            errors["user_update_password_error"] = "Please enter your password more than 8 characters"
        elif postData["user_update_password"] != postData["user_update_confirm_password"]:
            errors["user_update_password_error"] = "Confirm password must match with your password"

        return errors


class Admin(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AdminManager()


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    user_message = models.ForeignKey(
        User, related_name='user_message_id', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + " second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Comment(models.Model):
    message_id = models.ForeignKey(
        Message, related_name="comment_message_id", on_delete=models.CASCADE)
    user_comment = models.ForeignKey(
        User, related_name="comment_user_id", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def comment_whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + " second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"
