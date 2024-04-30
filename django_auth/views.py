from django.http import request, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from auth_app.models import Userform
from django.contrib.auth import authenticate, login
from django.contrib import messages


def Home(request):
    return render(request, 'Home.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        username = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')
        phone_no = request.POST.get('phone_no')
        dob = request.POST.get('dob')
        form1 = Userform(name=name, email=username, password=password, city=city, phone_no=phone_no, dob=dob)
        form1.save()
        return HttpResponseRedirect('/signup/')
    return render(request, 'Sign_up.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password1 = request.POST.get('password')
        user1 = authenticate(request, email=username, password=password1)
        if user1 is not None:
            login(request, user1)
            return HttpResponse('You Logged In')
        else:
            return HttpResponse('User is invalid')
    return render(request, 'Sign_in.html')

def dashboard(request):
    pass

def logout(request):
    pass
