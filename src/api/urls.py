from django.urls import path

from . import views

urlpatterns = [
    path('category', views.get_categories, name='category_list'),
    path('sample', views.get_samples, name='sample_list'),
    path('rates', views.get_rates, name='rate_list'),
]