from django.shortcuts import render

# Create your views here.


def index(request):
    r = request.get('https://db.fortnitetracker.com/weapons')
    print(r)
    return render(request, 'index.html')
