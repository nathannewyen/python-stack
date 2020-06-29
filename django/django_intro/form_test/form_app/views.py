from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def create_user(request):
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    return redirect('/success')


def success(request):
    return render(request, "success.html")
