from django.db import models
import re
import bcrypt

# Create your models here.


class UserManager(models.Manager):
    def userValidator(self, postData):
        errors = {}
        if len(postData['firstname']) < 2:
            errors['firstname'] = "Firstname of at least 2 characters required!"
        if len(postData['lastname']) < 2:
            errors['lastname'] = "Lastname of at least 2 characters required!"

        usernameMatch = User.objects.filter(username=postData['username'])

        if len(postData['username']) < 4:
            errors['reg_username'] = "Username of at least 3 characters required!"
# username validation on login
        elif len(usernameMatch) > 0:
            errors['Username_exists'] = "Username taken, please try again with a different Username."
# password Validation
        if postData['password'] != postData['password_confirm']:
            errors['password'] = "Password does not match!"

        elif len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters"
        return errors

    def loginValidator(self, postData):
        errors = {}
        # log In errors
        usernameMatch = User.objects.filter(username=postData['username'])

        if len(postData['username']) < 1:
            errors['username'] = "Enter your registered Username to Log In"
# username validation on login
        elif len(usernameMatch) == 0:
            errors['Username does not exist'] = "Invalid username, please use another Username or register!"
        # if the username is valid, verify if password match
        else:
            user = usernameMatch[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Password does not match"

        return errors


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=75)
    confirm_password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class FavoriteChamps(models.Model):
    name = models.CharField(max_length=255)
    favorite = models.ForeignKey(
        User, related_name='user_favorite', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
