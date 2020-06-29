from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
import datetime
# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def timedisplay(request):
    mydate = datetime.datetime.now()

    context = {
        "time": gmtime("%a-%b-%d %H:%M %p", localtime()),
        "mydate": mydate
    }
    return render(request, 'index.html', context)
