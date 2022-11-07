from django.urls import path
from .views import HomePage, Welcome, logoutUser

urlpatterns = [
    path('', Welcome, name="welcome-page"),
    path('home/', HomePage, name="home-page"),
    path('logout/', logoutUser, name="logout"),
]
