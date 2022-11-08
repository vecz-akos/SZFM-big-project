from django.http import JsonResponse
from .models import Category, Sample, Rate
from .serializers import CategorySerializer, SampleSerializer, RateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def get_categories(request):
    if request.method == "GET":
        category_filter = dict(request.GET.items())
        categories = Category.objects.filter(**category_filter)
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse({"categories": serializer.data}, safe=False)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "POST"])
def get_samples(request):
    if request.method == "GET":
        sample_filter = dict(request.GET.items())
        samples = Sample.objects.filter(**sample_filter)
        serializer = SampleSerializer(samples, many=True)
        return JsonResponse({"samples": serializer.data}, safe=False)
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
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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