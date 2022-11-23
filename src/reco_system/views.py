from django.shortcuts import render
from api.models import Samples, Rating

def main_view(request):
    return render(request, 'rate/rate.html', {})