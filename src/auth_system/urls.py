from django.urls import path
from .views import HomePage, Welcome, Register, Login, logoutUser

urlpatterns = [
    path('', Welcome, name="welcome-page"),
    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutUser, name="logout"),
]
