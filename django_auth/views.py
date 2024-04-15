from django.http import request
from django.shortcuts import render


def Home(request):
    return render(request, 'home.html')

def signin(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'Sign_up.html')

def logout(request):
    pass

