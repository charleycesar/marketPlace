from django.db import models
from customers.models import Customer


# Create your models here.
class StatusChoice(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=20)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Order(models.Model):
    total = models.FloatField()
    purchase_date = models.DateField()
    status = models.ForeignKey(StatusChoice, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    obs = models.CharField(max_length=500)

    def __str__(self):
        return self.status.name