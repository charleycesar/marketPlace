from django.contrib import admin
# Register your models here.
from .models import Order
from products.models import Item
class ItemInline(admin.TabularInline):
    model = Item

class OrderAdmin(admin.ModelAdmin):
  model = Order
  inlines = [ItemInline]


admin.site.register(Order, OrderAdmin)

