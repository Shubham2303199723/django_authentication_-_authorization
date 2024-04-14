from django.http import request
from django.shortcuts import render


def login(request):
    return render (request, 'index.html')

def register(request):
    pass

def logout(request):
    pass

