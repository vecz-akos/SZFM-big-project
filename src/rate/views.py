from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from rest_framework.response import Response
from rest_framework import status
from api.views import get_sample_data
from api.models import Sample, Category

from django.http import HttpResponse


@login_required
def select_sample(request, category):
    if (current_category := Category.objects.get(name=category)):
        category_id = current_category.id
        samples = get_sample_data({"categoryId": category_id})
        template = loader.get_template("rate/rate.html")
        context = {
            "samples": samples,
            "category_name": current_category.name,
            "user": request.user
        }
        #return HttpResponse(str(samples))
        #return render(request, 'templates/rate.html', {"samples": samples, "category_name": current_category.name, "user": request.user})
        return HttpResponse(template.render(context, request))
    return Response(status=status.HTTP_404_NOT_FOUND)

@login_required
def rate_sample(request, category, id):
    return render(request, 'rate/index.html', {})
