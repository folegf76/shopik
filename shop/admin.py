from django.contrib import admin
from .models import Category, Product, Subcategory, Brand, ProductsPhoto
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(ProductsPhoto)