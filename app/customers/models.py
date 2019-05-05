from django.db import models


# Create your models here.
class Place(models.Model):
    address = models.CharField(max_length=300)
    number = models.IntegerField()
    complement = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=14)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.address


class Customer(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    address = models.OneToOneField(Place, models.CASCADE)

    def __str__(self):
        return self.name
