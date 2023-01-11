from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from api.views import get_category_data, get_sample_data, get_samples_to_home_page
from reco_system.views import get_popular
from api.models import Category
import random


@login_required
def HomePage(request):
    categs = Category.objects.all()
    samps = get_popular(pc=8)
    ret_dict = get_samples_to_home_page()
    samples = get_sample_data()
    if len(samples) > 6:
        samples = random.sample(get_sample_data(), 6)
    else:
        samples = []
    return render(request, 'auth_system/index.html', {"categories": categs, "samples": samps, "user": request.user, "ret_dict": ret_dict, "samples":samples})

def Welcome(request):
    context = {
        "error_msg": ""
    }
    if request.method != 'POST':
        return render(request, 'auth_system/welcome.html', context)
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
            context["error_msg"] = "Bad username or password!"

    return render(request, 'auth_system/welcome.html', context)

def logoutUser(request):
    logout(request)
    return redirect('welcome-page')
