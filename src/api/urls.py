from django.urls import path

from . import views

urlpatterns = [
    path('category_list', views.get_categories, name='category_list'),
    path('sample_list', views.get_samples, name='sample_list'),
]