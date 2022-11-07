from django.http import JsonResponse
from .models import Category, Sample, Rate
from .serializers import CategorySerializer, SampleSerializer, RateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def get_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
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
        samples = Sample.objects.all()
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
        rates = Rate.objects.all()
        serializer = RateSerializer(rates, many=True)
        return JsonResponse({"rates": serializer.data}, safe=False)
    elif request.method == "POST":
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
