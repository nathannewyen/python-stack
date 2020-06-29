from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def process_money(request):

    request.session["activities"] = []
    # Add Money
    if "earn_gold" not in request.session.keys():

        request.session["earn_gold"] = 0
        request.session["activity_log"] = ""
    # End of Add money

        return render(request, 'index.html')


def increase_money(request):
    mydate = datetime.datetime.today().replace(microsecond=0)
    # Add money for farm
    request.session["space"] = request.POST["space"]
    if request.session["space"] == "0":
        request.session["random_gold"] = random.randint(10, 20)
        request.session["earn_gold"] += request.session["random_gold"]
        request.session["activity_log"] += "Earn " + str(
            request.session["random_gold"]) + " gold from the farm! (" + str(mydate) + ") \n"
    # End of farm

    # Add money for cave
    elif request.session["space"] == "1":
        request.session["random_gold"] = random.randint(5, 10)
        request.session["earn_gold"] += request.session["random_gold"]
        request.session["activity_log"] += "Earn " + str(
            request.session["random_gold"]) + " gold from the cave! (" + str(mydate) + ") \n"
    # End of cave

    # Add money for House
    elif request.session["space"] == "2":
        request.session["random_gold"] = random.randint(2, 5)
        request.session["earn_gold"] += request.session["random_gold"]
        request.session["activity_log"] += "Earn " + str(
            request.session["random_gold"]) + " gold from the house! (" + str(mydate) + ") \n"
    # End of House

    # Add money for casino
    else:
        request.session["random_gold"] = random.randint(-50, 50)

        if request.session["random_gold"] >= 0:
            request.session["earn_gold"] += request.session["random_gold"]
            request.session["activity_log"] += "Entered a casino and won " + str(
                request.session["random_gold"]) + " golds ... YAY!!! (" + str(mydate) + ") \n"
        else:
            if request.session["random_gold"] < 0:
                request.session["earn_gold"] += request.session["random_gold"]
                request.session["activity_log"] += "Entered a casino and lost " + str(
                    request.session["random_gold"]) + " golds ... OUCH!!! (" + str(mydate) + ") \n"
    # End of casino

    request.session["activities"].append(request.session["activity_log"])

    return redirect('/')


def decrease_money(request):
    request.session["random_gold"] = random.randint(1, 200)
    request.session["earn_gold"] -= request.session["random_gold"]
    return redirect('/')
