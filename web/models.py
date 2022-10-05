from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    price = models.FloatField()
    is_unit = models.BooleanField()
    is_bio = models.BooleanField()

class Farm(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    num = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    products = models.ManyToManyField(Product)
    contact = models.CharField(max_length=50)
