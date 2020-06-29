from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect('/')


def createDivs(request, numDivs):
    newarr = []

    for i in range(0, int(numDivs), 1):
        newarr.append(i)
    context = {
        'numbMessage': newarr,
        'numberDivs': numDivs
    }

    return render(request, 'index.html', context)


def edit(request, numDivs):
    newarr = []

    for i in range(0, int(numDivs), 1):
        newarr.append(i)
    context = {
        'numbMessage': newarr,
        'numberDivs': numDivs
    }

    return render(request, 'edit.html', context)


def delete(request, numDivs):
    return redirect("/")
