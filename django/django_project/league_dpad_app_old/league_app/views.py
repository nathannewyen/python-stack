from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from urllib.request import urlopen
import json
import bcrypt

# Create your views here.


def landing_page(request):
    if 'loggedinId' in request.session:
        loggedinUser = User.objects.get(id=request.session['loggedinId'])
        return redirect('/champions/')
    else:
        return render(request, "landing.html")


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def post_register(request):
    errorsFromValidator = User.objects.userValidator(request.POST)
    if len(errorsFromValidator) > 0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value, extra_tags="register")
        return redirect("/register/")

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                                  username=request.POST['username'], password=pw_hash, confirm_password=pw_hash)
    request.session['loggedinId'] = newUser.id
    return redirect(f'/user/{newUser.id}/')


def post_login(request):
    errorsFromValidator = User.objects.loginValidator(request.POST)
    if len(errorsFromValidator) > 0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value, extra_tags="login")
        return redirect("/login/")

    user = User.objects.get(username=request.POST['username'])
    request.session['loggedinId'] = user.id
    return redirect(f'/user/{user.id}/')


def user(request, id):
    if 'loggedinId' not in request.session:
        return redirect('/login/')
    loggedinUser = User.objects.get(id=request.session['loggedinId'])

    with urlopen("http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion.json") as response:
        source = response.read()

    data = json.loads(source)
    keys = data.keys()

    # Dictionary
    champdict = data.get('data')
    champ_data = champdict.values()

    context = {
        "loggedinUser": loggedinUser,
        'favorite_champs': User.objects.get(id=id).user_favorite.all(),
        'champ_data': champ_data,

    }
    return render(request, "user_page.html", context)


def champions_page(request):
    if 'loggedinId' not in request.session:
        return redirect('login')
    loggedinUser = User.objects.get(id=request.session['loggedinId'])

    with urlopen("http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion.json") as response:
        source = response.read()

    data = json.loads(source)
    keys = data.keys()

    # Dictionary
    champdict = data.get('data')
    champ_data = champdict.values()
    context = {
        "loggedinUser": loggedinUser,
        'champ_data': champ_data,
    }
    return render(request, "champions.html", context)


def logout(request):
    request.session.clear()
    return redirect('/login/')


def champ_info(request, id):
    if 'loggedinId' not in request.session:
        return redirect('/login/')
    loggedinUser = User.objects.get(id=request.session['loggedinId'])

    with urlopen("http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion.json") as response:
        source = response.read()

    data = json.loads(source)
    keys = data.keys()

    # Dictionary
    champdict = data.get('data')
    champ_data = champdict.values()
    for i in champ_data:
        print(i['image'])

    context = {
        "loggedinUser": loggedinUser,
        "champ_data": champ_data,
        'id': id,

    }
    return render(request, "champion_info.html", context)


def add(request, id):
    if 'loggedinId' not in request.session:
        return redirect('/login/')
    loggedinUser = User.objects.get(id=request.session['loggedinId'])

    favorite_champion = FavoriteChamps.objects.get_or_create(
        name=request.POST["name"], favorite=loggedinUser)

    with urlopen("http://ddragon.leagueoflegends.com/cdn/10.9.1/data/en_US/champion.json") as response:
        source = response.read()

    data = json.loads(source)
    keys = data.keys()

    # Dictionary
    champdict = data.get('data')
    champ_data = champdict.values()

    if not favorite_champion[1]:
        messages.error(request, "Already added to favorite list!",
                       extra_tags="add_error")
        return redirect(f"/champions/{id}/")

    return redirect(f'/user/{loggedinUser.id}/')


def remove(request, user_id, champ_id):
    if 'loggedinId' not in request.session:
        return redirect('/login/')
    loggedinUser = User.objects.get(id=request.session['loggedinId'])
    user = User.objects.get(id=user_id)
    user_favorite_champs = User.objects.get(id=user_id).user_favorite.all()
    champs_favorite = FavoriteChamps.objects.get(name=champ_id)

    if user.id == loggedinUser.id:
        champs_favorite.delete()

    return redirect(f"/user/{loggedinUser.id}/")
