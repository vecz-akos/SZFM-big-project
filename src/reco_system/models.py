from django.db import models
from django.contrib.auth.models import User

class Samples(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=300)
    img = models.ImageField(
        upload_to='imgs/', 
        height_field='height', 
        width_field='width'
    ),
    tags = models.CharField(max_length=50)
    def __str__(self):
        return str(self.pk)
