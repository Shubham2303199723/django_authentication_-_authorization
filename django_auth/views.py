from django.http import request
from django.shortcuts import render


def login(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'Sign_up.html')

def logout(request):
    pass

