from rest_framework.serializers import ModelSerializer
from .models import Category, Sample, Rate

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SampleSerializer(ModelSerializer):
    class Meta:
        model = Sample
        fields = "__all__"

class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"
