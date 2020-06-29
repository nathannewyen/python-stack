from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt
import re


# Create your views here.


def index(req):
    return render(req, 'index.html')


def wall(req):

    if req.session["login_status_and_id"]["status"]:
        context = {
            "first_name": User.objects.get(id=req.session["login_status_and_id"]["login_id"]).first_name,
            "last_name":  User.objects.get(id=req.session["login_status_and_id"]["login_id"]).last_name,
            "post_data": Message.objects.all(),
            "comment_data": Comment.objects.all(),
            "user_id": User.objects.get(id=req.session["login_status_and_id"]["login_id"]).id,
        }

    return render(req, 'wall.html', context)


def register(req):
    return render(req, 'register_login.html')


def process(req):
    for key in ("first_name", "last_name", "email", "password"):
        req.session[key] = req.POST[key]

    first_name = req.session["first_name"]
    last_name = req.session["last_name"]
    email = req.session["email"]

    # Hashed password
    hashed_pw = bcrypt.hashpw(
        req.POST["password"].encode(), bcrypt.gensalt()).decode()

    errors = User.objects.validation(req.POST)

    # Valid data
    if len(errors):
        for key, value in errors.items():
            messages.error(req, value, extra_tags=key)
        return redirect("/register/")

    elif len(User.objects.filter(email=email)) > 0:
        errors["duplicated_email_error"] = "This email is already taken"
        return redirect("/register/")

    else:
        User.objects.create(first_name=first_name,
                            last_name=last_name, email=email, password=hashed_pw)

        user = User.objects.filter(email=req.POST["email"])

        # Login status and user id --> save as session
        req.session["login_status_and_id"] = {
            "status": True,
            "login_id": User.objects.get(email=req.POST["email"]).id
        }

        return redirect('/user/')


def login(req):
    if len(req.POST["login-password"]) < 1:
        messages.error(req, "Please enter your password",
                       extra_tags="login_pass_error")
        return redirect("/register/")

    if len(req.POST["login-email"]) < 1:
        messages.error(req, "Please enter your email",
                       extra_tags="login_error")
        return redirect("/register/")

    #  Email not Valid
    elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(req.POST["login-email"]):
        messages.error(
            req, "Please enter valid email form (eg. abc123@gmail.com)", extra_tags="login_error")
        return redirect("/register/")

    elif len(User.objects.filter(email=req.POST["login-email"])) < 1:
        messages.error(req, "Email is not exist please try again!",
                       extra_tags="login_error")
        return redirect("/register/")

    # Check password
    elif not bcrypt.checkpw(req.POST["login-password"].encode(), User.objects.get(email=req.POST["login-email"]).password.encode()):
        messages.error(req, "Wrong password please try again",
                       extra_tags="login_pass_error")
        return redirect("/register/")
    # Login Success
    else:
        messages.success(req, "Successfully, logged in!",
                         extra_tags="login_success")
        req.session["login_status_and_id"] = {
            "status": True,
            "login_id": User.objects.get(email=req.POST["login-email"]).id
        }
    user = User.objects.filter(email=req.POST["login-email"])
    logged_user = user[0]
    req.session["user_id"] = logged_user.id
    return redirect("/user/")


def user(req):
    if req.session["login_status_and_id"]["status"]:
        context = {
            "first_name": User.objects.get(id=req.session["login_status_and_id"]["login_id"]).first_name,
            "last_name":  User.objects.get(id=req.session["login_status_and_id"]["login_id"]).last_name,
            "id": User.objects.get(id=req.session["login_status_and_id"]["login_id"]).id,

        }

    return render(req, 'user.html', context)

# Logout and clear session browser


def logout(req):
    req.session.clear()
    return redirect("/")


# Post Message to Wall
def post_message(req):
    user_id = req.session["user_id"]

    user = User.objects.get(id=user_id)

    Message.objects.create(user_id=user, message=req.POST["post_message"])
    messages.success(req, "Message successfully posted")
    return redirect('/wall/')

# Post comment to a message


def post_comment(req):
    user_id = req.session["user_id"]
    user = User.objects.get(id=user_id)
    message = Message.objects.get(id=req.POST['message_id'])

    Comment.objects.create(message_id=message, user_id=user,
                           comment=req.POST["comment"])
    messages.success(req, "Comment successfully posted")
    return redirect("/wall/")


def delete_comment(req, id):
    delete_comment = Comment.objects.get(id=id)
    print(delete_comment.id)
    delete_comment.delete()
    return redirect("/wall/")
