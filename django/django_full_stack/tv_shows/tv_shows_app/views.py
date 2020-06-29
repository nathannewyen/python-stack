from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_show_info(request):
    all_shows = Show.objects.all()
    context = {
        "all_shows": all_shows,
    }

    return render(request, 'all_show_info.html', context)


def single_show_info(request, id):
    show = Show.objects.get(id=id)
    context = {
        'id': id,
        'show': show
    }
    return render(request, 'single_show_info.html', context)


def new_show(request):
    return render(request, 'new_show.html')


def create(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new/')
    elif len(Show.objects.filter(title=request.POST["title"])) > 0:
        errors["duplicated_title_error"] = "This title is already existed"
        messages.error(
            request, errors["duplicated_title_error"], extra_tags="duplicated_title_error")
        return redirect('/shows/new/')
    else:
        this_show = Show.objects.create(
            title=request.POST["title"], network=request.POST["network"],
            release_date=request.POST["release_date"], description=request.POST["description"])

    return redirect(f"/shows/{this_show.id}")


def show_edit(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show,
        'id': id
    }
    return render(request, 'edit_show.html', context)


def update(request, id):
    show = Show.objects.get(id=id)
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show.id}/edit")
    elif len(Show.objects.filter(title=request.POST["title"])) > 0:
        errors["duplicated_title_error"] = "This title is already existed"
        messages.error(
            request, errors["duplicated_title_error"], extra_tags="duplicated_title_error")
        return redirect(f"/shows/{show.id}/edit")
    else:
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.release_date = request.POST["release_date"]
        show.description = request.POST["description"]
        show.save()
    return redirect(f"/shows/{show.id}")


def delete(request, id):
    show = Show.objects.get(id=id)
    if request.method == "GET":
        show.delete()
    return redirect("/shows")


def validate_title(request):
    title = request.GET.get('title', None)
    data = {
        'is_taken': Show.objects.filter(title__iexact=title).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'This title is already exists.'
    return JsonResponse(data)
