from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    img = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Sample(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    img = models.CharField(max_length=500, null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Rate(models.Model):
    rateValues = (
        ("-1", -1),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5)
    )
    
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    sampleId = models.ForeignKey(Sample, on_delete=models.CASCADE)
    rate = models.SmallIntegerField(default=rateValues[0], choices=rateValues)
    datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("userId", "sampleId")

    def __str__(self):
        return f"user={self.userId},sample={self.sampleId},rate={self.rate}"
