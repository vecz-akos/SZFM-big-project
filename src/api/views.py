from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json

def get_categories(request):
    category_filter = {k: v for k, v in request.GET.items()}
    res = json.dumps([str(c) for c in models.Category.objects.filter(**category_filter)])
    return HttpResponse(res, content_type="application/json")

def get_samples(request):
    sample_filter = {k: v for k, v in request.GET.items()}
    res = json.dumps([str(c) for c in models.Sample.objects.filter(**sample_filter)])
    return HttpResponse(res, content_type="application/json")
