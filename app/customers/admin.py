from django.contrib import admin

# Register your models here.
from .models import Customer, Place


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'full_name', 'active', 'address',)

admin.site.register(Customer)
admin.site.register(Place)