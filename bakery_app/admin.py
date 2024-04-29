from django.contrib import admin

from . models import Contact
from . models import Subscribing
from . models import Order
from . models import Products
# Register your models here.

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'message'
    ]

admin.site.register(Subscribing)

@admin.register(Products)
class AdminProduct(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'description',
        'image'
    ]

admin.site.register(Order)