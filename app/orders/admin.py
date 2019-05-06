from django.contrib import admin
# Register your models here.
from .models import Order, StatusChoice
from products.models import Item, TypeUnity
from customers.models import Customer


class ItemInline(admin.TabularInline):
    model = Item
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "type_unity":
            kwargs["queryset"] = TypeUnity.objects.filter(active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [ItemInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "customer":
            kwargs["queryset"] = Customer.objects.filter(active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusChoice)
admin.site.register(TypeUnity)
