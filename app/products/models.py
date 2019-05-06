from django.db import models
from categories.models import Category
from orders.models import Order

# Create your models here.
class TypeUnity(models.Model):
    name = models.CharField(max_length=120)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,models.CASCADE)
    price = models.FloatField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Item(models.Model):
    unity = models.IntegerField()
    type_unity = models.ForeignKey(TypeUnity, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.product.name
