from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from api.views import get_category_data, get_sample_data


@login_required
def HomePage(request):
    categs = get_category_data()
    samps = get_sample_data()
    return render(request, 'auth_system/index.html', {"categories": categs, "samples": samps})

def Welcome(request):
    if request.method != 'POST':
        return render(request, 'auth_system/welcome.html', {})
    if "signup" in request.POST:
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        user_name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('passw')

        new_user = User.objects.create_user(user_name, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name

        new_user.save()

        return redirect('welcome-page')
    elif "login" in request.POST:
        user_name = request.POST.get('uname')
        password = request.POST.get('passw')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Wrong Username or password')

    return render(request, 'auth_system/welcome.html', {})

def logoutUser(request):
    logout(request)
    return redirect('welcome-page')