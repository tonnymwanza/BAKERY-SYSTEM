from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

class Subscribing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='the_subscriber')


class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(null=True)

class Order(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.products.name