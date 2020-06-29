from django.db import models
import re

# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # Check first name
        if len(postData["first_name"]) == 0:
            errors["first_name_error"] = "First name is required ( Not accepted blank first name )"
        elif len(postData["first_name"]) <= 1:
            errors["first_name_error"] = "First name should be longer"
        elif len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be longer"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["first_name"]):
            errors[
                "first_name_error"] = "First name should be greater than or equal to 2 characters, letter only ( Not accepted numbers or special characters )"

        # Check last name
        if len(postData["last_name"]) == 0:
            errors["last_name_error"] = "Last name is required ( Not accepted blank first name )"
        elif len(postData["last_name"]) <= 1:
            errors["last_name_error"] = "Last name should be longer"
        elif len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be longer"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["last_name"]):
            errors[
                "last_name_error"] = "Last name should be greater than or equal to 2 characters, letter only ( Not accepted numbers or special characters )"

        # Check email
        emailMatch = User.objects.filter(email=postData["email"])
        if len(emailMatch) > 0:
            errors["email_error"] = "This email is already taken"

        elif len(postData["email"]) < 1:
            errors["email_error"] = "Email should longer"

        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["email"]):
            errors["email_error"] = "Please enter valid email form (eg. abc123@gmail.com)"

        # Check password
        if len(postData["password"]) < 1:
            errors["password_error"] = "Please enter your password ( Not accepted blank password )"
        elif len(postData["password"]) and len(postData["confirm-password"]) < 8:
            errors["password_error"] = "Please enter your password more than 8 characters"
        elif postData["password"] != postData["confirm-password"]:
            errors["password_error"] = "Confirm password must match with your password"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __unicode__(self):
        return "id : " + str(self.id) + ", first_name : " + self.first_name + ", last_name : " + self.last_name + ", email : " + self.email + ", password : " + str(self.password) + ", created_at : " + str(self.created_at) + ", updated_at : " + str(self.updated_at)
