from django.http import JsonResponse
from .models import Category, Sample, Rate
from .serializers import CategorySerializer, SampleSerializer, RateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def get_category_data(filter={}):
    categories = Category.objects.filter(**filter)
    serializer = CategorySerializer(categories, many=True)
    return serializer.data

def get_sample_data(filter={}):
    samples = Sample.objects.filter(**filter)
    serializer = SampleSerializer(samples, many=True)
    return serializer.data

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
        serializer = RateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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