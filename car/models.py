from django.db import models


# Create your models here.

class Cars(models.Model):
    brand = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()