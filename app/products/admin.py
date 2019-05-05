from django.contrib import admin
from products.models import Item


# Register your models here.
from .models import Product

admin.site.register(Product)

