from django.http import JsonResponse
from .models import Category, Sample, Rate
from .serializers import CategorySerializer, SampleSerializer, RateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from random import sample
from reco_system.views import get_random_sample

def get_category_data(filter={}):
    categories = Category.objects.filter(**filter)
    serializer = CategorySerializer(categories, many=True)
    return serializer.data

def get_sample_data(filter={}):
    samples = Sample.objects.filter(**filter)
    serializer = SampleSerializer(samples, many=True)
    return serializer.data

def add_rate(sample_id, user_id, rate_num):
    data = {"userId": user_id, "sampleId": sample_id, "rate": rate_num}
    serializer = RateSerializer(data=data)
    if serializer.is_valid() and not is_rate_in_db(user_id, sample_id):
        serializer.save()
        return "ok"
    return serializer.errors

def is_rate_in_db(user_id, sample_id):
    return Rate.objects.filter(**{"userId": user_id, "sampleId": sample_id}).exists()

def get_rate_data(sample_id, user_id):
    return Rate.objects.filter(**{"userId": user_id, "sampleId": sample_id})

def get_samples_to_home_page(cat_num=3, samp_num=6):
    """
    Visszatér egy két dimenziós listával, minden sorban különböző
    kategóriákkal, és soronként különböző mintákkal.
    """
    cats = list(Category.objects.values("id", "name"))
    if len(cats) > cat_num:
        cats = sample(cats, cat_num)
    ret_dict = {}
    for category in cats:
        samps = get_random_sample(category["id"], samp_num)
        ret_dict[category["name"]] = samps
    return ret_dict

@api_view(["GET", "POST"])
def get_categories(request):
    if request.method == "GET":
        category_filter = dict(request.GET.items())
        data = get_category_data(category_filter)
        return JsonResponse({"categories": data}, safe=False)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "POST"])
def get_samples(request):
    if request.method == "GET":
        sample_filter = dict(request.GET.items())
        data = get_sample_data(sample_filter)
        return JsonResponse({"samples": data}, safe=False)
    elif request.method == "POST":
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "POST"])
def get_rates(request):
    if request.method == "GET":
        rate_filter = dict(request.GET.items())
        rates = Rate.objects.filter(**rate_filter)
        serializer = RateSerializer(rates, many=True)
        return JsonResponse({"rates": serializer.data}, safe=False)
    elif request.method == "POST":
        data = {key: request.data.get(key) for key in ["userId", "sampleId", "rate"]}
        rate = add_rate(**data)
        if rate == "ok":
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(rate, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET", "PUT", "DELETE"])
def get_category_details(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)