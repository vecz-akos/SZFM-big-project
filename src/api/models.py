from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, null=True)
    img = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.name}"

class Sample(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    img = models.CharField(max_length=500, null=True)
    tags = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f"{self.name}"

class Rate(models.Model):
    class RateValue(models.IntegerChoices):
        NOT_FILLED = -1
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    sampleId = models.ForeignKey(Sample, on_delete=models.CASCADE)
    rate = models.SmallIntegerField(default=RateValue.NOT_FILLED, choices=RateValue.choices)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user={self.userId},sample={self.sampleId},rate={self.rate}"
