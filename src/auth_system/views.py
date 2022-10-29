from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def HomePage(request):
    return render(request, 'auth_system/index.html', {})

def Register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        user_name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('passw')

        new_user = User.objects.create_user(user_name, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name

        new_user.save()

        return redirect('login-page')

    return render(request, 'auth_system/register.html', {})

def Login(request):
    if request.method == 'POST':
        user_name = request.POST.get('uname')
        password = request.POST.get('passw')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'auth_system/login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('login-page')