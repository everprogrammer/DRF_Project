from django.contrib import admin
from .models import CustomUser, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller')

admin.site.register(Product, ProductAdmin)