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

# def signin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         user1 = authenticate(request, username=username, password=password)
#         print(user1)
#         if user1 is not None:
#             login(request, user1)
#             return HttpResponse('You Logged In')
#         else:
#             return HttpResponse('User is invalid')
#     return render(request, 'Sign_in.html')

def dashboard(request):
    pass

def logout(request):
    pass


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Userform.objects.get(email=email)
            if user.check_password(password):
                # Authentication successful
                request.session['user_id'] = user.id
                return redirect('dashboard')
            else:
                # Invalid password
                messages.error(request, 'Invalid email or password')
        except Userform.DoesNotExist:
            # User does not exist
            messages.error(request, 'Invalid email or password')

    return render(request, 'Sign_in.html')