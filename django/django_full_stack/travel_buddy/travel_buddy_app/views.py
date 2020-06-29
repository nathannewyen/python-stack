from django.shortcuts import render, redirect
from .models import User, Trip
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    errors = User.objects.register_validator(request.POST)
    # Check Valid Registration
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    # Create User
    else:
        hashed_pw = bcrypt.hashpw(
            request.POST["password"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            name=request.POST["fname"], username=request.POST["username"], password=hashed_pw)

        # Login status and user id saves in session
        request.session["user_id"] = user.id

        return redirect("/travels/")


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    else:
        user = User.objects.filter(username=request.POST["login_username"])
        logged_user = user[0]
        request.session["user_id"] = logged_user.id
        return redirect("/travels/")


def logout(request):
    request.session.clear()
    return redirect("/")


def user(request):
    user = User.objects.get(id=request.session["user_id"])

    context = {
        'user': User.objects.get(id=request.session["user_id"]),
        'trip_user': User.objects.get(id=request.session["user_id"]).user_plan.all(),
        'all_trip': Trip.objects.all(),
    }
    return render(request, 'user.html', context)


def destination(request, id):
    trip = Trip.objects.get(id=id)

    context = {
        'trip': Trip.objects.get(id=id),
        'user_join': Trip.objects.get(id=id).join.all(),
    }

    return render(request, 'destination.html', context)


def add_trip(request):
    return render(request, 'add_trip.html')


def add_trip_process(request):
    user_id = request.session["user_id"]
    user = User.objects.get(id=user_id)

    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/travels/add/")

    else:
        trip = Trip.objects.create(
            destination=request.POST["destination"],
            description=request.POST["description"],
            plan_by=user,
            travel_from=request.POST["from"],
            travel_to=request.POST["to"]
        )

        return redirect("/travels/")


def join(request, id):
    trip = Trip.objects.get(id=id)
    user_id = request.session["user_id"]
    trip.join.add(user_id)
    trip.save()
    return redirect(f'/travels/destination/{trip.id}')


def delete(request, id):
    trip = Trip.objects.get(id=id)
    user_id = request.session["user_id"]
    trip.delete()
    return redirect("/travels/")
