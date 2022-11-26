from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from rest_framework.response import Response
from rest_framework import status
from api.views import get_sample_data, get_sample_data, add_rate, is_rate_in_db, get_rate_data
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
    if not (current_sample := get_sample_data({"id":id})):
        return Response(status=status.HTTP_404_NOT_FOUND)
    current_sample = current_sample[0]
    context = {
        "user": request.user,
        "rate": -1,
        "sample": current_sample,
        "user": request.user
    }

    if request.method == "GET":
        options = [t[0] for t in Rate.rate.field.choices[1:]]
        context["options"] = options
        rate = get_rate_data(user_id = request.user.id, sample_id = current_sample["id"])
        if rate.exists(): # már értékelte a user
            context["rate"] = rate.get().rate
        return render(request, 'rate/rate.html', context)
    elif request.method == "POST":
        rate = add_rate(sample_id=current_sample["id"], user_id=context["user"].id, rate_num=request.POST["rate"])
        if rate == "ok":
            context["rate"] = rate_num=request.POST["rate"]
            return render(request, 'rate/rate.html', context)
    return Response(status=status.HTTP_404_NOT_FOUND)
