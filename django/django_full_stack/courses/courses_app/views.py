from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.


def index(request):

    context = {
        'courses': Course.objects.all(),
    }

    return render(request, 'index.html', context)


def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for key in errors.keys():
            messages.error(request, errors[key])
        return redirect('/')
    else:
        Course.objects.create(
            name=request.POST["name"], description=request.POST["description"])

    return redirect("/")


def destroy(request, id):
    this_course = Course.objects.get(id=id)
    context = {
        'this_course': this_course
    }
    return render(request, 'destroy.html', context)


def delete(request, id):
    delete_this_course = Course.objects.get(id=id)
    delete_this_course.delete()
    return redirect("/")
