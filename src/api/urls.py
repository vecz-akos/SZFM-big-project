from django.urls import path

from . import views

urlpatterns = [
    path('category', views.get_categories, name='category_list'),
    path('category/<int:id>', views.get_category_details, name='category_detail'),
    path('sample', views.get_samples, name='sample_list'),
    path('rate', views.get_rates, name='rate_list'),
]