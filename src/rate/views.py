from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from rest_framework.response import Response
from rest_framework import status
from api.views import get_sample_data, get_sample_data
from api.models import Sample, Category, Rate
from api.serializers import RateSerializer
from django.http import HttpResponse


@login_required
def select_sample(request, category):
    if (current_category := Category.objects.get(name=category)):
        category_id = current_category.id
        samples = get_sample_data({"categoryId": category_id})
        template = loader.get_template("rate/category.html")
        context = {
            "samples": samples,
            "category_name": current_category.name,
            "user": request.user
        }
        return HttpResponse(template.render(context, request))
    return Response(status=status.HTTP_404_NOT_FOUND)

@login_required
def rate_sample(request, category, id):
    context = {
        "user": request.user,
        "rated": False
    }
    if request.method == "GET":
        if (current_sample := get_sample_data({"id":id})):
            current_sample = current_sample[0]
            options = [t[0] for t in Rate.rate.field.choices[1:]]
            context["sample"] = current_sample
            context["user"] = request.user
            context["options"] = options
            if Rate.objects.filter(userId = request.user.id, sampleId = current_sample["id"]): # már értékelte a user
                context["rated"] = True
                return render(request, 'rate/rate.html', context)
            return render(request, 'rate/rate.html', context)
    elif request.method == "POST":
        data = {key: request.POST[key] for key in ["userId", "sampleId", "rate"]}
        serializer = RateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)
