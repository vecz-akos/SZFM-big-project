from django.urls import path

from . import views

urlpatterns = [
    path('<slug:category>', views.select_sample, name='select_sample'),
    path('<slug:category>/<int:id>', views.rate_sample, name='rate_sample'),
]