from django.http import HttpResponse
from django.shortcuts import render
import random
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def home(request):
    return render(request, 'generator/home.html', {'title': 'Главная страница'})

def about(request):
    return render(request, 'generator/about.html', {'title': 'О сайте'})


def password(request):
    characters = list(ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))
    if request.GET.get('numbers'):
        characters.extend(list(digits))
    if request.GET.get('special'):
        characters.extend(list(punctuation))

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'title': 'Ваш пароль','password': thepassword})
