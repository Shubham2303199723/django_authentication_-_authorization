from django.http import request
from django.shortcuts import render


def Home(request):
    return render(request, 'Home.html')

def signup(request):
    if request.methpd == 'POST':
        Name = None
    return render(request, 'Sign_up.html')

def signin(request):
    return render(request, 'Sign_in.html')

def dashboard(request):
    pass

def logout(request):
    pass


