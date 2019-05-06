from django.contrib import admin


# Register your models here.
from .models import Product
from categories.models import Category


class ProductAdmin(admin.ModelAdmin):
    model = Product

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(status=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Product, ProductAdmin)

