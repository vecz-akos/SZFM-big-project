from django.urls import path
from .views import HomePage, Welcome, Register, Login, logoutUser

urlpatterns = [
    path('home/', HomePage, name="home-page"),
    path('welcome/', Welcome, name="welcome-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutUser, name="logout"),
]
