from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from auth_app.models import Userform


def Home(request):
    return render(request, 'Home.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')
        phone_no = request.POST.get('phone_no')
        dob = request.POST.get('dob')
        form = Userform(name=name, email=email, password=password, city=city, phone_no=phone_no, dob=dob)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('signin')
    return render(request, 'Sign_up.html')

def signin(request):
    if request.method == "POST":
        name = request.session.get('name')
        password = request.session.get('password')
        form = Userform(name=name, password=password)
        return HttpResponseRedirect('/home/')
    return render(request, 'Sign_in.html')



def dashboard(request):
    pass

def logout(request):
    pass


