from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt
import re

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    for key in ("first_name", "last_name", "email", "password"):
        request.session[key] = request.POST[key]

    first_name = request.session["first_name"]
    last_name = request.session["last_name"]
    email = request.session["email"]

    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    elif len(User.objects.filter(email=email)) > 0:
        errors["duplicated_email_error"] = "This email is already existed"
        messages.error(
            request, errors["duplicated_email_error"], extra_tags="duplicated_email_error")
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(
            request.POST["password"].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_pw
        )
        # login status & user id --> saves at session

        request.session["login_status_and_id"] = {
            "status": True, "login_id": User.objects.get(email=request.POST["email"]).id}

        # Redirect route with message
        messages.success(request, "Successfully, registered!",
                         extra_tags="registration_success")
        return redirect("/success/")


def login(request):
    if len(request.POST["login_password"]) < 1:
        messages.error(request, "Enter your password",
                       extra_tags="login_pass_error")

    if len(request.POST["login_email"]) < 1:
        messages.error(request, "Enter your email",
                       extra_tags="login_error")
        return redirect("/")

    # If Email not valid
    elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(request.POST["login_email"]):
        messages.error(
            request, "Please enter valid email form (eg. abc123@gmail.com)", extra_tags="login_error")
        return redirect("/")

    # If Email not exist
    elif len(User.objects.filter(email=request.POST["login_email"])) < 1:
        messages.error(request, "Email is not exist", extra_tags="login_error")
        return redirect("/")

    # If Email valid and exist
    else:
        # check user password matched with database using bcrypt library
        if not bcrypt.checkpw(request.POST["login_password"].encode(), User.objects.get(email=request.POST["login_email"]).password.encode()):
            messages.error(
                request, "Wrong password, please check your password again", extra_tags="login_pass_error")
            return redirect("/")

        # Case : successful login
        else:
            messages.success(request, "Successfully, logged in!",
                             extra_tags="login_success")

            # change login status with user id ( #### be careful not to save sensitive user information on session #### )
            request.session["login_status_and_id"] = {
                "status": True, "login_id": User.objects.get(email=request.POST["login_email"]).id}
            return redirect("/success")


def success(request):
    if request.session["login_status_and_id"]["status"]:
        context = {
            "first_name": User.objects.get(id=request.session["login_status_and_id"]["login_id"]).first_name,
            "last_name": User.objects.get(id=request.session["login_status_and_id"]["login_id"]).last_name,
        }
        return render(request, 'user.html', context)

    # redirect with error message if user does not logged in
    else:
        messages.error(request, "Login error", extra_tags="login_error")
        redirect("/")


def clear(request):
    del request.session["login_status_and_id"]
    return redirect("/")
