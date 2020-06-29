from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    return render(request, 'index.html')


def random_word(request):
    if "number_count" not in request.session.keys():
        request.session["number_count"] = 0
    else:
        request.session["number_count"] += 1
    random_word_generate = get_random_string(length=32)
    context = {
        "random_number_count": request.session["number_count"],
        'random_word_generate': random_word_generate
    }
    return render(request, 'random_word.html', context)


def clear(request):
    request.session['number_count'] = 0
    return redirect('/random_word')
